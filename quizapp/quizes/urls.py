from django.urls import path
from .views import(
    QuizListView,
    quiz_view,
)

app_name='quizes'

urlpatterns = [
    path('home/',QuizListView.as_view(),name='main_view'),
    path('home/<uuid:quiz_id>',quiz_view,name='quiz_view')
]

