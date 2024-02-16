from django.urls import path
from .views import ListPost


urlpatterns = [
    path('', ListPost.as_view()),
]
