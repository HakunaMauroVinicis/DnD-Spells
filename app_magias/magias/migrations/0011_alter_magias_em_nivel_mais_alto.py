# Generated by Django 5.1 on 2024-08-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magias', '0010_magias_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magias',
            name='em_nivel_mais_alto',
            field=models.TextField(null=True),
        ),
    ]