# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testando', '0004_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursoturma',
            fields=[
                ('id_cursoturma', models.AutoField(primary_key=True, serialize=False, verbose_name='id_cursoturma')),
                ('ano_ofertado', models.ForeignKey(db_column='ano_ofertado', on_delete=django.db.models.deletion.CASCADE, related_name='ctano_ofertado', to='testando.Disciplinaofertada')),
                ('cod_turma', models.ForeignKey(db_column='cod_turma', on_delete=django.db.models.deletion.CASCADE, related_name='ctcod_turma', to='testando.Turma')),
                ('nome_disciplina', models.ForeignKey(db_column='nome_disciplina', on_delete=django.db.models.deletion.CASCADE, related_name='ctnome_disciplina', to='testando.Disciplina')),
                ('semestre_ofertado', models.ForeignKey(db_column='semestre_ofertado', on_delete=django.db.models.deletion.CASCADE, related_name='ctsemestre_ofertado', to='testando.Disciplinaofertada')),
                ('sigla_curso', models.ForeignKey(db_column='sigla_curso', on_delete=django.db.models.deletion.CASCADE, to='testando.Curso')),
            ],
            options={
                'db_table': 'cursoturma',
            },
        ),
    ]
