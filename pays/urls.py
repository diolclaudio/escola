from django.urls import path
from . import views

app_name = 'pays'

urlpatterns = [
    path('', views.index, name='index'),
    path('pagamentos/', views.pay, name='pay'),
    path('confirmar/<int:id>', views.confirmar, name='confirmar'),
    path('info/', views.info, name='info'),
    path('comentario/', views.comentario, name='comentario'),
    path('alunos/', views.alunos, name='alunos' ),
    path('horario/', views.hor, name='hor'),
    path('melhores_alunos/', views.mel, name='mel'),
    path('professores/', views.prof, name='prof')
 ]
