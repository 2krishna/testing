from django.urls import path
from .views import PsychometricTestView, DBDATestView, QuestionView

urlpatterns = [

    path('question/', DBDATestView.as_view({'post': 'create'})),
    path('psychometric/', PsychometricTestView.as_view({'post': 'create', 'get': 'list'})),
    path('q/', QuestionView.as_view({'post': 'create'})),

]
