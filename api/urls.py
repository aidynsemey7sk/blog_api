from django.urls import path
from .views import ListPost, DetailPost

urlpatterns = [
    path('<int:pk>/', DetailPost.as_view()),
    path('/', ListPost.as_view()),
]
