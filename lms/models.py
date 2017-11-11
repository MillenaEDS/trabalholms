from django.db import models

# Create your models here.

class Curso(models.Model):
    sigla = models.CharField('sigla', primary_key=True, max_length=5)
    nome = models.CharField('nome', unique=True, max_length=50)

    class Meta:
        db_table = 'curso'

class Gradecurricular(models.Model):
    sigla_curso = models.OneToOneField('Curso', models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    ano = models.SmallIntegerField()
    semestre = models.CharField('semestre', max_length=1)

    class Meta:
        db_table = 'gradecurricular'
        unique_together = (('sigla_curso', 'ano', 'semestre'),)

class Periodo(models.Model):
    sigla_curso = models.OneToOneField('Gradecurricular', models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    ano_grade = models.ForeignKey('Gradecurricular', models.DO_NOTHING, db_column='ano_grade', related_name = 'Periodo.ano_grade+')
    semestre_grade = models.ForeignKey('Gradecurricular', models.DO_NOTHING, db_column='semestre_grade', related_name = 'Periodo.semestre_grade+')
    numero = models.IntegerField()

    class Meta:
        db_table = 'periodo'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade', 'numero'),)

class Disciplina(models.Model):
    nome = models.CharField('nome', primary_key=True, max_length=240)
    carga_horaria = models.IntegerField()
    teoria = models.DecimalField(max_digits=4, decimal_places=2)
    pratica = models.DecimalField(max_digits=4, decimal_places=2)
    ementa = models.CharField('ementa', max_length=500)
    competencias = models.CharField('competencias', max_length=500)
    habilidades = models.CharField('habilidades', max_length=500)
    conteudo = models.CharField('conteudo', max_length=500)
    bibliografia_basica = models.CharField('bibliografia basica', max_length=500)
    bibliografia_complementar = models.CharField('bibliografia complementar', max_length=500)

    class Meta:
        db_table = 'disciplina'

class Disciplinaofertada(models.Model):
    nome_disciplina = models.OneToOneField('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano = models.SmallIntegerField()
    semestre = models.CharField('semestre', max_length=1)

    class Meta:
        db_table = 'disciplinaofertada'
        unique_together = (('nome_disciplina', 'ano', 'semestre'),)

class Periododisciplina(models.Model):
    sigla_curso = models.OneToOneField('Periodo', models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    ano_grade = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='ano_grade', related_name = 'Periododisciplina.ano_grade+')
    semestre_grade = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='semestre_grade', related_name = 'Periododisciplina.semestre_grade+')
    numero_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='numero_periodo', related_name = 'Periododisciplina.numero_periodo+')
    nome_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='nome_disciplina', related_name = 'Periododisciplina.nome_disciplina+')

    class Meta:
        db_table = 'periododisciplina'
        unique_together = (('sigla_curso', 'ano_grade', 'semestre_grade', 'numero_periodo', 'nome_disciplina'),)

class Aluno(models.Model):
    ra = models.AutoField('ra', primary_key=True)
    nome = models.CharField('nome', max_length=120)
    email = models.CharField('email', max_length=80)
    celular = models.CharField('celular', max_length=11)
    sigla_curso = models.CharField('sigla_curso', max_length=5)

    class Meta:
        db_table = 'aluno'

class Professor(models.Model):
    ra = models.AutoField('ra', primary_key=True)
    apelido = models.CharField('apelido', unique=True, max_length=30)
    nome = models.CharField('nome', max_length=120)
    email = models.CharField('email', max_length=80)
    celular = models.CharField('celular', max_length=11)

    class Meta:
        db_table = 'professor'

class Turma(models.Model):
    nome_disciplina = models.OneToOneField('Disciplinaofertada', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='ano_ofertado', related_name = 'Turma.ano_ofertado+')
    semestre_ofertado = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='semestre_ofertado', related_name = 'Turma.semestre_ofertado+')
    id = models.CharField('id', max_length=1)
    turno = models.CharField('turno', max_length=15)
    ra_professor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='ra_professor')

    class Meta:
        db_table = 'turma'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id'),)

class Cursoturma(models.Model):
    sigla_curso = models.OneToOneField('Curso', models.DO_NOTHING, db_column='sigla_curso', primary_key=True)
    nome_disciplina = models.ForeignKey('Turma', models.DO_NOTHING, db_column='nome_disciplina', related_name = 'Cursoturma.nome_disciplina+')
    ano_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='ano_ofertado', related_name = 'Cursoturma.ano_ofertado+')
    semestre_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='semestre_ofertado', related_name = 'Cursoturma.semestre_ofertado+')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', related_name = 'Cursoturma.id_turma+')

    class Meta:
        db_table = 'cursoturma'
        unique_together = (('sigla_curso', 'nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma'),)

class Matricula(models.Model):
    ra_aluno = models.OneToOneField('Aluno', models.DO_NOTHING, db_column='ra_aluno', primary_key=True)
    nome_disciplina = models.ForeignKey('Turma', models.DO_NOTHING, db_column='nome_disciplina', related_name = 'Matricula.nome_disciplina+')
    ano_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='ano_ofertado', related_name = 'Matricula.ano_ofertado+')
    semestre_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='semestre_ofertado', related_name = 'Matricula.semestre_ofertado+')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', related_name = 'Matricula.id_turma+')

    class Meta:
        db_table = 'matricula'
        unique_together = (('ra_aluno', 'nome_disciplina', 'ano_ofertado', 'id_turma'),)

class Questao(models.Model):
    nome_disciplina = models.OneToOneField('Turma', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='ano_ofertado', related_name = 'Questao.ano_ofertado+')
    semestre_ofertado = models.ForeignKey('Turma', models.DO_NOTHING, db_column='semestre_ofertado', related_name = 'Questao.semestre_ofertado+')
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', related_name = 'Matricula.id_turma+')
    numero = models.IntegerField()
    data_limite_entrega = models.DateField()
    descricao = models.CharField('descricao', max_length=500)
    dta = models.DateField()

    class Meta:
        db_table = 'questao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero'),)

class Arquivoquestao(models.Model):
    nome_disciplina = models.OneToOneField('Questao', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='ano_ofertado', related_name = 'Arquivoquestao.ano_ofertado+')
    semestre_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='semestre_ofertado', related_name = 'Arquivoquestao.semestre_ofertado+')
    id_turma = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_turma', related_name = 'Arquivoquestao.id_turma+')
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao', related_name = 'Arquivoquestao.numero_questao+')
    arquivo = models.CharField('arquivo', max_length=500)

    class Meta:
        db_table = 'arquivoquestao'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'arquivo'),)

class Resposta(models.Model):
    nome_disciplina = models.OneToOneField('Questao', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='ano_ofertado', related_name = 'Resposta.ano_ofertado+')
    semestre_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='semestre_ofertado', related_name = 'Resposta.semestre_ofertado+')
    id_turma = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_turma', related_name = 'Resposta.id_turma+')
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao', related_name = 'Resposta.numero_questao+')
    ra_aluno = models.ForeignKey('Aluno', models.DO_NOTHING, db_column='ra_aluno')
    data_avaliacao = models.DateField()
    nota = models.DecimalField('nota', max_digits=4, decimal_places=2)
    avaliacao = models.CharField('avaliacao', max_length=500)
    descricao = models.CharField('descricao', max_length=500)
    data_de_envio = models.DateField()

    class Meta:
        db_table = 'resposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno'),)

class Arquivoresposta(models.Model):
    nome_disciplina = models.OneToOneField('Questao', models.DO_NOTHING, db_column='nome_disciplina', primary_key=True)
    ano_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='ano_ofertado', related_name = 'Arquivoresposta.ano_ofertado+')
    semestre_ofertado = models.ForeignKey('Questao', models.DO_NOTHING, db_column='semestre_ofertado', related_name = 'Arquivoresposta.semestre_ofertado+')
    id_turma = models.ForeignKey('Questao', models.DO_NOTHING, db_column='id_turma', related_name = 'Arquivoresposta.id_turma+')
    numero_questao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='numero_questao', related_name = 'Arquivoresposta.numero_questao+')
    ra_aluno = models.ForeignKey('Aluno', models.DO_NOTHING, db_column='ra_aluno')
    arquivo = models.CharField('arquivo', max_length=500)

    class Meta:
        db_table = 'arquivoresposta'
        unique_together = (('nome_disciplina', 'ano_ofertado', 'semestre_ofertado', 'id_turma', 'numero_questao', 'ra_aluno', 'arquivo'),)
