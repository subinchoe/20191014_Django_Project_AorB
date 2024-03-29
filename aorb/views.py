from django.shortcuts import render, redirect
from .models import Question, Choice
import random

# Create your views here.

def random_pick(request):
    questions = Question.objects.all()
    if questions:
        question = random.choice(questions)

        return redirect('aorb:detail', question.id)
    else:
        return redirect('aorb:index')

def detail(request, id):
    question = Question.objects.get(id=id)

    if question.choice_set.all():
        cnt_a = question.choice_set.filter(pick="1").count()
        cnt_b = question.choice_set.filter(pick="2").count()
        cnt_all = cnt_a + cnt_b
        ratio_a = "{:.1f}".format(cnt_a / cnt_all * 100)
        ratio_b = "{:.1f}".format(cnt_b / cnt_all * 100)

        cnt = {
            'ratio_a': ratio_a,
            'ratio_b': ratio_b,
        }
    else:
        cnt = {
            'ratio_a': '0.0',
            'ratio_b': '0.0',
        }

    context = {
        'question' : question,
        'cnt': cnt,
    }
    print(cnt)
    return render(request, 'detail.html', context)

def index(request):
    context = {
        'questions': Question.objects.all()
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":

        Question.objects.create(
            ask=request.POST.get('ask'),
            itemA=request.POST.get('itemA'),
            itemB=request.POST.get('itemB')
        )

        return redirect('aorb:index')
    else:
        return render(request, "form.html")

def comment_create(request, question_id):
    if request.method == "POST":
        pick = request.POST.get('pick')    
        comment = request.POST.get('comment')
        question = Question.objects.get(id=question_id)

        Choice.objects.create(
            pick=pick,
            comment=comment,
            question=question
        )

        return redirect('aorb:detail', question_id)

def comment_delete(request, question_id, choice_id):
    Choice.objects.get(id=choice_id).delete()

    return redirect('aorb:detail', question_id)

def update(request, id):
    question = Question.objects.get(id=id)
    if request.method == "POST":
        ask = request.POST.get('ask')
        itemA = request.POST.get('itemA')
        itemB = request.POST.get('itemB')

        question.ask = ask
        question.itemA = itemA
        question.itemB = itemB
        question.save()

        return redirect('aorb:detail', id)

    else:
        context = {
            'question': question,
        }
        return render(request, 'form.html', context)

def delete(request, id):
    Question.objects.get(id=id).delete()

    return redirect('aorb:index')

def search(request):
    keyword = request.GET.get('keyword')
    
    questions = Question.objects.filter(ask__icontains=keyword)
    
    context = {
        'questions': questions,
    }

    return render(request, 'index.html', context)