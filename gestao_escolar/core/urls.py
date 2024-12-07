from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('cadastro-aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    path('importar-alunos/', views.importar_alunos, name='importar_alunos'),
    path('cadastro-turma/', views.cadastro_turma, name='cadastro_turma'),
    path('matricular-aluno/', views.matricular_aluno, name='matricular_aluno'),
    path('alunos/', views.aluno_lista, name='aluno_lista'),  # Define a URL para a lista de alunos
    path('aluno/lista/', views.aluno_lista, name='aluno_lista'),
    path('aluno/editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('aluno/deletar/<int:id>/', views.deletar_aluno, name='deletar_aluno'),  # Adiciona a URL para deletar aluno

    path('notas/registrar/<int:aluno_id>/', views.registrar_notas, name='registrar_notas'),
    path('frequencia/registrar/<int:aluno_id>/', views.registrar_frequencia, name='registrar_frequencia'),
    path('boletim/<int:aluno_id>/', views.gerar_boletim, name='boletim'),

    path('cadastro-professor/', views.cadastro_professor, name='cadastro_professor'),
    path('cadastro-turma/', views.cadastro_turma, name='cadastro_turma'),
    path('cadastro-materia/', views.cadastro_materia, name='cadastro_materia'),
    path('atribuir-professor/', views.atribuir_professor, name='atribuir_professor'),
    path('professores/', views.lista_professores, name='lista_professores'),
    path('professor/editar/<int:id>/', views.editar_professor, name='editar_professor'),  # URL para editar
    path('area-alunos/', views.area_alunos, name='area_alunos'),
    path('area_administracao/', views.area_administracao, name='area_administracao'),
]
