from django.urls import path, re_path, include

from .views import QuizViewSet, QuestionViewSet

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    re_path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/quiz/', QuizViewSet.as_view({'get': 'list'})),
    path('api/v1/quiz/<int:pk>', QuestionViewSet.as_view({'get': 'list'})),
]
