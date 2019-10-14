from django.urls import path
from . import views


app_name="aorb"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),

    path('<int:id>/', views.create_comment, name="create_comment"),

    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),
]
