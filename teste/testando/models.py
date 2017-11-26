from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)
    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=50)
    ra = models.IntegerField(unique=True)
    password = models.CharField(max_length=150)
    perfil = models.CharField(max_length=1, default='C')
    ativo = models.BooleanField(default=True)
    

    USERNAME_FIELD = 'ra' #campo que usa como usuario
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()
    
    @property
    def is_staff(self):
        return self.perfil == 'C'

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.nome
    def get_full_name(self):
        return self.nome

    def __str__ (self):
        return self.nome


class Curso(models.Model):
    id_curso = models.AutoField('id_curso',primary_key=True)
    ativo = models.BooleanField(default=True)
    sigla = models.CharField('sigla', unique=True, max_length=5, null=False)
    nome = models.CharField('nome', unique=True, max_length=50, null=False)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.sigla
    
    class Meta:
        db_table = 'Curso'

class Gradecurricular(models.Model):
    id_gradecurricular = models.AutoField('id_gradecurricular',primary_key=True)
    sigla_curso = models.ForeignKey(to='curso', related_name='sigla_curso', db_column='sigla_curso', null=False)
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(null=False, max_length=1)
    
    def __str__(self):
        return '%s - %s - %s' % (self.sigla_curso, self.ano, self.semestre)
    
    class Meta:
        db_table = 'gradecurricular'

class Periodo(models.Model):
    id_periodo = models.AutoField('id_periodo',primary_key=True)
    sigla_curso = models.ForeignKey(to='curso', related_name='psigla_curso', db_column='sigla_curso', null=False)
    ano_grade = models.ForeignKey(to='gradecurricular', related_name='ano_grade', db_column='ano_grade', null=False)
    semestre_grade = models.ForeignKey(to='gradecurricular',  related_name='semestre_grade', db_column='semestre_grade', null=False)
    numero = models.IntegerField('numero', null=False)
    
    def __str__(self):
        return '%s - %s' % (self.semestre_grade, self.numero)
    
    class Meta:
        db_table = 'periodo'

class Aluno(Usuario):
    email = models.CharField('email', max_length=80, null=False)
    celular = models.CharField('celular', max_length=11, null=False)
    sigla_curso = models.ForeignKey(to='Curso', related_name="asigla_curso",db_column='sigla_curso', null=False)
    
    def __str__(self):
        return '%s' % int(self.ra)
    
    class Meta:
        db_table = 'Aluno'

class Professor(Usuario):
    apelido = models.CharField('apelido', unique=True, max_length=30)
    email = models.CharField('email', max_length=80, null=False)
    celular = models.CharField('celular', max_length=11, null=False)

    def __str__(self):
        return '%s' % int(self.ra)

    class Meta:
        db_table = 'professor'

class Disciplina(models.Model):
    nome = models.CharField('nome', unique=True, max_length=240)
    carga_horaria = models.IntegerField('carga_horaria', null=False)
    teoria = models.DecimalField('teoria',max_digits=4, decimal_places=2, null=False)
    pratica = models.DecimalField('pratica',max_digits=4, decimal_places=2, null=False)
    ementa = models.CharField('ementa', max_length=500, null=False)
    competencias = models.CharField('competencias', max_length=500, null=False)
    habilidades = models.CharField('habilidades', max_length=500, null=False)
    conteudo = models.CharField('conteudo', max_length=500, null=False)
    bibliografia_basica = models.CharField('bibliografia basica', max_length=500, null=False)
    bibliografia_complementar = models.CharField('bibliografia complementar', max_length=500, null=False)
    
    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'disciplina'

class Disciplinaofertada(models.Model):
    id_disciplinaofertada = models.AutoField('id_disciplinaofertada',primary_key=True)
    nome_disciplina = models.ForeignKey(to='Disciplina', related_name="nome_disciplina", db_column='nome_disciplina', unique=True)
    ano = models.SmallIntegerField('ano',null=False)
    semestre = models.CharField('semestre', max_length=1, null=False)
    
    def __str__(self):
        return '%s - %s - %s' % (self.nome_disciplina, self.ano, self.semestre)

    class Meta:
        db_table = 'disciplinaofertada'

class Periododisciplina(models.Model):
    id_periododisciplina = models.AutoField('id_periododisciplina', primary_key=True)
    sigla_curso = models.ForeignKey(to='curso', related_name = 'pdsigla_curso', db_column='sigla_curso', null=False)
    ano_grade = models.ForeignKey(to='gradecurricular', related_name = 'pdano_grade', db_column='ano_grade', null=False)
    semestre_grade = models.ForeignKey(to='gradecurricular', related_name = 'pdsemestre_grade', db_column='semestre_grade', null=False)
    numero_periodo = models.ForeignKey(to='Periodo', related_name = 'pdnumero_periodo', db_column='numero_periodo', null=False)
    nome_disciplina = models.ForeignKey(to='Disciplina', related_name = 'pdnome_disciplina', db_column='nome_disciplina', null=False)
    
    def __str__(self):
        return '%s - %s' % (self.numero_periodo, self.nome_disciplina)
    
    class Meta:
        db_table = 'periododisciplina'



class Turma(models.Model):
    id_turma = models.AutoField('id_turma', primary_key=True)
    nome_disciplina = models.ForeignKey(to='Disciplina', related_name = 'tnome_disciplina', db_column='nome_disciplina', null=False)
    ano_ofertado = models.ForeignKey(to='Disciplinaofertada', related_name = 'tano_ofertado', db_column='ano_ofertado', null=False)
    semestre_ofertado = models.ForeignKey(to='Disciplinaofertada', related_name = 'tsemestre_ofertado', db_column='semestre_ofertado', null=False)
    turma = models.CharField('turma', max_length=1, null=False)
    turno = models.CharField('turno', max_length=15, null=False)
    ra_professor = models.ForeignKey(to='Professor', related_name = 'tra_professor', db_column='ra_professor', null=False)
    
    def __str__(self):
        return '%s - %s - %s - %s' % (self.ano_ofertado, self.turma, self.turno, self.ra_professor)
    
    class Meta:
        db_table = 'turma'

class Cursoturma(models.Model):
    id_cursoturma = models.AutoField('id_cursoturma', primary_key=True)
    sigla_curso = models.ForeignKey(to='Curso', db_column='sigla_curso')
    nome_disciplina = models.ForeignKey(to='disciplina', related_name = 'ctnome_disciplina', db_column='nome_disciplina',null=False)
    ano_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'ctano_ofertado', db_column='ano_ofertado',null=False)
    semestre_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'ctsemestre_ofertado', db_column='semestre_ofertado', null=False)
    cod_turma = models.ForeignKey(to='Turma', related_name = 'ctcod_turma', db_column='cod_turma', null=False)

    def __str__(self):
        return '%s - %s' % (self.sigla_curso,  self.cod_turma)

    class Meta:
        db_table = 'cursoturma'

class Matricula(models.Model):
    id_matricula = models.AutoField('id_matricula', primary_key=True)
    ra_aluno = models.ForeignKey(to='Aluno', db_column='ra_aluno', null=False)
    nome_disciplina = models.ForeignKey(to='disciplina', related_name = 'mnome_disciplina', db_column='nome_disciplina', null=False)
    ano_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'mano_ofertado', db_column='ano_ofertado', null=False)
    semestre_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'msemestre_ofertado', db_column='semestre_ofertado', null=False)
    cod_turma = models.ForeignKey(to='Turma', related_name = 'mcod_turma', db_column='cod_turma', null=False)

    def __str__(self):
        return '%s - %s' % (self.ra_aluno, self.cod_turma)

    class Meta:
        db_table = 'matricula'

class Questao(models.Model):
    id_questao = models.AutoField('id_questao', primary_key=True)
    cod_turma = models.ForeignKey(to='Turma', related_name = 'qid_turma', db_column='id_turma', null=False)
    nome_disciplina = models.ForeignKey(to='disciplina', related_name = 'qnome_disciplina', db_column='nome_disciplina', null=False)
    ano_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'qano_ofertado', db_column='ano_ofertado', null=False)
    semestre_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'qsemestre_ofertado', db_column='semestre_ofertado', null=False)   
    numero = models.IntegerField('numero', null=False)
    descricao = models.CharField('descricao', max_length=750, null=False)
    data_limite_entrega = models.DateField('data_limite_entrega', null=False)
    arquivo = models.FileField(upload_to="arquivos/")

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.cod_turma, self.numero, self.data_limite_entrega, self.descricao, self.dta)
    
    class Meta:
        db_table = 'questao'

'''class Arquivoquestao(models.Model):
    id_arquivoquestao = models.AutoField('id_arquivoquestao', primary_key=True)
    nome_disciplina = models.ForeignKey(to='disciplina', related_name = 'aqnome_disciplina', db_column='nome_disciplina', null=False)
    ano_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'aqano_ofertado', db_column='ano_ofertado', null=False)
    semestre_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'aqsemestre_ofertado', db_column='semestre_ofertado', null=False)
    id_turma = models.ForeignKey(to='Turma', related_name = 'aqid_turma', db_column='id_turma', null=False)
    numero_questao = models.ForeignKey(to='questao', related_name= 'aqnumero_questao', db_column='numero_questao', null=False)
    arquivo = models.CharField('arquivo', max_length=750, null=False)
    
    def __str__(self):
        return '%s - %s' % (self.numero_questao, self.arquivo)
    
    class Meta:
        db_table = 'arquivoquestao'

class Resposta(models.Model):
    id_resposta = models.AutoField('id_resposta', primary_key=True)
    nome_disciplina = models.ForeignKey(to='disciplina', related_name = 'rnome_disciplina', db_column='nome_disciplina', null=False)
    ano_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'rano_ofertado', db_column='ano_ofertado', null=False)
    semestre_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'rsemestre_ofertado', db_column='semestre_ofertado', null=False)
    id_turma = models.ForeignKey(to='Turma', related_name = 'rid_turma', db_column='id_turma', null=False)
    numero_questao = models.ForeignKey(to='questao', related_name= 'rnumero_questao', db_column='numero_questao', null=False)
    ra_aluno = models.ForeignKey(to='Aluno', related_name= 'raluno', db_column='ra_aluno', null=False)
    data_avaliacao = models.DateField('data_avaliacao', null=False)
    nota = models.DecimalField('nota', max_digits=4, decimal_places=2, null=False)
    avaliacao = models.CharField('avaliacao', max_length=500, null=False)
    descricao = models.CharField('descricao', max_length=500, null=False)
    data_de_envio = models.DateField('data_de_envio', null=False)
    
    def __str__(self):
        return '%s - %s - %s - %s - %s - %s' % (self.numero_questao, self.data_avaliacao, self.nota, self.avaliacao, self.descricao, self.data_de_envio)
    
    class Meta:
        db_table = 'resposta'

class Arquivoresposta(models.Model):
    id_arquivoresposta = models.AutoField('id_arquivoresposta', primary_key=True)
    nome_disciplina = models.ForeignKey(to='disciplina', related_name = 'arnome_disciplina', db_column='nome_disciplina', null=False)
    ano_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'arano_ofertado', db_column='ano_ofertado', null=False)
    semestre_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'arsemestre_ofertado', db_column='semestre_ofertado', null=False)
    id_turma = models.ForeignKey(to='Turma', related_name = 'arid_turma', db_column='id_turma', null=False)
    numero_questao = models.ForeignKey(to='questao', related_name= 'arnumero_questao', db_column='numero_questao', null=False)
    ra_aluno = models.ForeignKey(to='Aluno', related_name= 'araluno', db_column='ra_aluno', null=False)
    arquivo = models.CharField('arquivo', max_length=500)

    def __str__(self):
        return '%s - %s' % (self.numero_questao, self.arquivo)

    class Meta:
        db_table = 'arquivoresposta' '''