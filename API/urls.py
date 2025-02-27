from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views.web_views import home
from .views.api_views import AlunoViewSet 


router = DefaultRouter()
router.register("alunos", AlunoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', home)
]