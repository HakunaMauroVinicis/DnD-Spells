# Generated by Django 5.1 on 2024-08-27 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Componentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Escolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Magias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('nivel', models.IntegerField(max_length=2)),
                ('tempo_conjuracao', models.TextField()),
                ('duracao', models.CharField(max_length=50)),
                ('alcance', models.CharField(max_length=50)),
                ('descicao', models.TextField()),
                ('em_nivel_mais_alto', models.TextField()),
                ('ritual', models.BooleanField(default=False)),
                ('concentracao', models.BooleanField(default=False)),
                ('ataque_magico', models.BooleanField(default=False)),
                ('tipo_dado', models.CharField(max_length=20, null=True)),
                ('savaguarda', models.CharField(max_length=50, null=True)),
                ('truque', models.BooleanField(default=False)),
                ('classes', models.ManyToManyField(to='magias.classes', verbose_name='classes_magias')),
                ('componentes', models.ManyToManyField(to='magias.componentes', verbose_name='componentes_magias')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magias.escolas', verbose_name='escola_magia')),
                ('fonte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magias.fonte', verbose_name='magia_fonte')),
            ],
        ),
    ]