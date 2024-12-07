from django import forms
from .models import Aluno, Professor, Turma, Materia, Atribuicao, Matricula

# Formulário para cadastro de Aluno
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_completo', 'data_nascimento', 'cpf', 'rg', 'telefone', 'email', 'endereco', 'nome_responsavel', 'historico_academico']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),  # Formato de data HTML5
        }


# Formulário para cadastro de Turma
class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome_turma', 'ano_letivo', 'turno', 'capacidade_maxima']

# Formulário para matrícula de Aluno em Turma
class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'turma']

# Formulário para cadastro de Professor
class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome_completo', 'horario_disponibilidade', 'contato_telefone', 'contato_email', 'endereco', 'disciplinas']
        widgets = {
            'disciplinas': forms.CheckboxSelectMultiple(),  # Exibe as disciplinas como checkboxes
        }
# Formulário para cadastro de Matéria
class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nome_materia', 'descricao']

# Formulário para atribuição de Professor a Turma e Matéria
class AtribuicaoForm(forms.ModelForm):
    class Meta:
        model = Atribuicao
        fields = ['professor', 'turma', 'materia', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),  # Formato de data HTML5
            'data_fim': forms.DateInput(attrs={'type': 'date'}),  # Formato de data HTML5
        }