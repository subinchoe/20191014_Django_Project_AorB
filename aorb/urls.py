from django.urls import path
from . import views


app_name="aorb"
urlpatterns = [
    path('', views.index, name="index"),

    path('create/', views.create, name="create"),
    path('<int:id>/detail/', views.detail, name="detail"),

    path('random/', views.random_pick, name="random_pick"),

    path('<int:question_id>/comment/', views.comment_create, name="comment_create"),
    path('<int:question_id>/comment/<int:choice_id>/delete', views.comment_delete, name="comment_delete"),

    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),

    path('search/', views.search, name="search"),
]