from django.contrib import admin
from .models import Aluno, Turma, Matricula, Nota, Frequencia, Boletim, Professor, Materia, Atribuicao

# Registro dos modelos no admin
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_nascimento', 'email')
    search_fields = ('nome_completo', 'cpf', 'email')
    list_filter = ('data_nascimento',)
    ordering = ('nome_completo',)

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome_turma', 'ano_letivo', 'turno', 'capacidade_maxima')
    search_fields = ('nome_turma', 'ano_letivo')
    list_filter = ('turno', 'ano_letivo')
    ordering = ('ano_letivo', 'nome_turma')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'turma', 'data_matricula')
    search_fields = ('aluno__nome_completo', 'turma__nome_turma')
    list_filter = ('turma',)
    ordering = ('data_matricula',)

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'bimestre', 'nota')
    search_fields = ('aluno__nome_completo', 'disciplina')
    list_filter = ('bimestre', 'disciplina')
    ordering = ('aluno', 'bimestre')

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'data', 'presente')
    search_fields = ('aluno__nome_completo',)
    list_filter = ('presente', 'data')
    ordering = ('data',)

@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'data_geracao')
    search_fields = ('aluno__nome_completo',)
    ordering = ('data_geracao',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'contato_email')
    search_fields = ('nome_completo', 'contato_email')
    filter_horizontal = ('disciplinas',)  # Adiciona uma interface para selecionar disciplinas


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome_materia', 'descricao')
    search_fields = ('nome_materia',)
    ordering = ('nome_materia',)

@admin.register(Atribuicao)
class AtribuicaoAdmin(admin.ModelAdmin):
    list_display = ('professor', 'turma', 'materia', 'data_inicio', 'data_fim')
    search_fields = ('professor__nome_completo', 'turma__nome_turma', 'materia__nome_materia')
    list_filter = ('data_inicio', 'data_fim')
    ordering = ('data_inicio',)
