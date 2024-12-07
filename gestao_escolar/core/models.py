from django.db import models

# Modelo para o Aluno
class Aluno(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=20)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField()
    nome_responsavel = models.CharField(max_length=255)
    historico_academico = models.TextField()

    def __str__(self):
        return self.nome_completo

# Modelo para Turma
class Turma(models.Model):
    nome_turma = models.CharField(max_length=50)  # Ex: 6º Ano A
    ano_letivo = models.IntegerField()  # Ano letivo (ex: 2024)
    turno = models.CharField(
        max_length=10, choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')]
    )  # Turno da turma
    capacidade_maxima = models.IntegerField()  # Capacidade máxima de alunos

    def __str__(self):
        return f"{self.nome_turma} - {self.ano_letivo}"

# Modelo para Matricula
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome_completo} - {self.turma.nome_turma}"

# Modelo para Matéria
class Materia(models.Model):
    # Lista de matérias predefinidas
    MATEMATICA = 'Matematica'
    PORTUGUES = 'Portugues'
    HISTORIA = 'Historia'
    GEOGRAFIA = 'Geografia'
    CIENCIAS = 'Ciencias'
    INGLES = 'Ingles'
    ARTE = 'Arte'
    EDUCACAO_FISICA = 'Educacao Fisica'
    RELIGIAO = 'Religiao'
    FILOSOFIA = 'Filosofia'

    MATERIAS_CHOICES = [
        (MATEMATICA, 'Matemática'),
        (PORTUGUES, 'Português'),
        (HISTORIA, 'História'),
        (GEOGRAFIA, 'Geografia'),
        (CIENCIAS, 'Ciências'),
        (INGLES, 'Inglês'),
        (ARTE, 'Arte'),
        (EDUCACAO_FISICA, 'Educação Física'),
        (RELIGIAO, 'Religião'),
        (FILOSOFIA, 'Filosofia'),
    ]

    nome_materia = models.CharField(
        max_length=100,
        choices=MATERIAS_CHOICES,  # Tornando a matéria um campo de escolha
        default=MATEMATICA  # Valor padrão
    )
    descricao = models.TextField(blank=True, null=True)  # Descrição opcional

    def __str__(self):
        return self.get_nome_materia_display()

# Modelo para Nota
class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Materia, on_delete=models.CASCADE)  # Agora vincula a Materia
    bimestre = models.IntegerField(choices=[(1, '1º Bimestre'), (2, '2º Bimestre'), (3, '3º Bimestre'), (4, '4º Bimestre')])
    nota = models.DecimalField(max_digits=5, decimal_places=2)  # Notas com 2 casas decimais

    def __str__(self):
        return f"{self.aluno.nome_completo} - {self.disciplina} - {self.bimestre}"

# Modelo para Frequência
class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=False)  # True se presente, False se ausente

    def __str__(self):
        return f"Frequência de {self.aluno.nome_completo} em {self.data}"

# Modelo para Boletim Escolar
class Boletim(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_geracao = models.DateField(auto_now_add=True)
    notas = models.ManyToManyField(Nota)
    frequencias = models.ManyToManyField(Frequencia)

    def __str__(self):
        return f"Boletim de {self.aluno.nome_completo} - {self.data_geracao}"

# Modelo para Professor
class Professor(models.Model):
    nome_completo = models.CharField(max_length=200)
    horario_disponibilidade = models.CharField(max_length=100)  # Horários de disponibilidade
    contato_telefone = models.CharField(max_length=15)  # Telefone de contato
    contato_email = models.EmailField()  # E-mail de contato
    endereco = models.TextField()  # Endereço completo
    disciplinas = models.ManyToManyField('Materia', related_name='professores')  # Relacionamento com Materia

    def __str__(self):
        return self.nome_completo


# Modelo para Atribuição de Professor a Matéria
class Atribuicao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.professor.nome_completo} - {self.turma.nome_turma} - {self.materia.nome_materia}"
