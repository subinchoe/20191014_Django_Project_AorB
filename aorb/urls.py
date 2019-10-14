from django.urls import path
from . import views


app_name="aorb"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),

    path('<int:question_id>/', views.comment_create, name="comment_create"),

    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),
]
