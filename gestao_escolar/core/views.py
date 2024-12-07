from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm, ProfessorForm, TurmaForm, MateriaForm, AtribuicaoForm, MatriculaForm
from django.http import HttpResponse
from django.contrib import messages
import pandas as pd
from .models import Aluno, Professor, Turma, Materia, Atribuicao, Matricula, Nota, Frequencia, Boletim

def home(request):
    return render(request, 'home.html')

def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno cadastrado com sucesso!")
            return redirect('aluno_lista')
    else:
        form = AlunoForm()
    return render(request, 'alunos/cadastro_aluno.html', {'form': form})

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)  # Obtém o aluno pelo ID
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()  # Salva as alterações no aluno
            return redirect('alunos/aluno_lista')  # Redireciona para a lista de alunos
    else:
        form = AlunoForm(instance=aluno)  # Carrega os dados do aluno no formulário

    return render(request, 'alunos/editar_aluno.html', {'form': form, 'aluno': aluno})

# View para deletar aluno
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)  # Obtém o aluno pelo ID
    aluno.delete()  # Exclui o aluno
    return redirect('alunos/aluno_lista.html')  # Redireciona para a lista de alunos

def aluno_lista(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/aluno_lista.html', {'alunos': alunos})

def importar_alunos(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        try:
            # Verifica o tipo de arquivo
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:
                messages.error(request, "Tipo de arquivo não suportado. Envie um CSV ou Excel.")
                return redirect('importar_alunos')

            # Itera sobre o DataFrame e salva os alunos
            for index, row in df.iterrows():
                Aluno.objects.create(
                    nome_completo=row['nome_completo'],
                    data_nascimento=row['data_nascimento'],
                    cpf=row['cpf'],
                    rg=row['rg'],
                    telefone=row['telefone'],
                    email=row['email'],
                    endereco=row['endereco'],
                    nome_responsavel=row['nome_responsavel'],
                    historico_academico=row['historico_academico']
                )
            
            messages.success(request, "Alunos importados com sucesso!")
            return redirect('aluno_lista')

        except Exception as e:
            messages.error(request, f"Erro ao importar alunos: {str(e)}")
            return redirect('importar_alunos')

    return render(request, 'alunos/importar_alunos.html')

def registrar_notas(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    disciplinas = Materia.MATERIAS_CHOICES  # Obtemos a lista predefinida de disciplinas

    if request.method == 'POST':
        disciplina = request.POST['disciplina']
        bimestre = int(request.POST['bimestre'])
        nota = float(request.POST['nota'])

        # Cria ou atualiza a nota do aluno
        Nota.objects.create(aluno=aluno, disciplina=disciplina, bimestre=bimestre, nota=nota)
        return redirect('boletim', aluno_id=aluno.id)

    return render(request, 'notas/registrar_notas.html', {'aluno': aluno, 'disciplinas': disciplinas})
# Lançar frequência diária
def registrar_frequencia(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    if request.method == 'POST':
        data = request.POST['data']
        presente = request.POST.get('presente', False)

        Frequencia.objects.create(aluno=aluno, data=data, presente=presente)
        return redirect('boletim', aluno_id=aluno.id)

    return render(request, 'notas/registrar_frequencia.html', {'aluno': aluno})

# Gerar boletim
def gerar_boletim(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    boletim = Boletim.objects.filter(aluno=aluno).first()  # Busca o boletim do aluno
    
    if not boletim:
        boletim = Boletim.objects.create(aluno=aluno)
    
    boletim.notas.set(Nota.objects.filter(aluno=aluno))
    boletim.frequencias.set(Frequencia.objects.filter(aluno=aluno))

    # Calcular a média de notas e frequência
    notas = boletim.notas.all()
    frequencias = boletim.frequencias.all()

    media_notas = sum([nota.nota for nota in notas]) / len(notas) if notas else 0
    taxa_frequencia = sum([1 for f in frequencias if f.presente]) / len(frequencias) * 100 if frequencias else 0

    # Alerta para alunos com baixa frequência
    alerta_frequencia = 'Alerta: Frequência abaixo de 75%' if taxa_frequencia < 75 else ''

    return render(request, 'notas/boletim.html', {
        'aluno': aluno,
        'boletim': boletim,
        'media_notas': media_notas,
        'taxa_frequencia': taxa_frequencia,
        'alerta_frequencia': alerta_frequencia
    })

def cadastro_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Turma cadastrada com sucesso!")
            return redirect('cadastro_turma')
    else:
        form = TurmaForm()
    
    return render(request, 'turmas/cadastro_turma.html', {'form': form})

def matricular_aluno(request):
    form = MatriculaForm()  # Inicializa o form de forma padrão fora do if

    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            # Verifica a capacidade da turma
            turma = form.cleaned_data['turma']
            total_alunos = Matricula.objects.filter(turma=turma).count()

            if total_alunos < turma.capacidade_maxima:
                form.save()
                return redirect('matricular_aluno')
            else:
                form.add_error('turma', 'A turma já atingiu a capacidade máxima de alunos.')
    
    return render(request, 'alunos/matricular_aluno.html', {'form': form})

def cadastro_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o professor e as disciplinas associadas
            return redirect('lista_professores')  # Redirecione conforme necessário
    else:
        form = ProfessorForm()
    
    return render(request, 'professores/cadastro_professor.html', {'form': form})

def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'professores/lista_professores.html', {'professores': professores})

def editar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('lista_professores')
    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'professores/editar_professor.html', {'form': form, 'professor': professor})

def cadastro_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Matéria cadastrada com sucesso!")
            return redirect('cadastro_materia')
    else:
        form = MateriaForm()

    return render(request, 'cadastro_materia.html', {'form': form})

def atribuir_professor(request):
    if request.method == 'POST':
        form = AtribuicaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Professor atribuído com sucesso!")
            return redirect('atribuir_professor')
    else:
        form = AtribuicaoForm()

    return render(request, 'atribuir_professor.html', {'form': form})

def area_alunos(request):
    # Lógica para exibir a área dos alunos
    return render(request, 'alunos/area_alunos.html')

def area_administracao(request):
    return render(request, 'area_administracao.html')