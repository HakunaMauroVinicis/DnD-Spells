# Generated by Django 5.1 on 2024-08-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magias', '0004_rename_descicao_magias_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='magias',
            name='alvo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='magias',
            name='savaguarda',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
