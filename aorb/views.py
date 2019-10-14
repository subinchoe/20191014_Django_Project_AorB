from django.shortcuts import render, redirect
from .models import Question
import random

# Create your views here.

def index(request):
    questions = Question.objects.all()
    if questions:

        question = random.choice(questions)

        context = {
            'question' : question,
        }

    else:
        context = {
            'question' : 0,
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

def create_comment(request, id):
    print(type(request.POST.get('pick')), request.POST.get('comment'))
    pass

def update(request, id):
    if request.method == "POST":
        ask = request.POST.get('ask')
        itemA = request.POST.get('itemA')
        itemB = request.POST.get('itemB')

        question = Question.objects.get(id=id)
        question.ask = ask
        question.itemA = itemA
        question.itemB = itemB
        question.save()

        context = {
            'question' : question,
        }
        return render(request, 'index.html', context)

    else:
        question = Question.objects.get(id=id)

        context = {
            'question': question,
        }
        return render(request, 'form.html', context)

def delete(request, id):
    Question.objects.get(id=id).delete()

    return redirect('aorb:index')
