# Generated by Django 5.1 on 2024-08-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magias', '0005_magias_alvo_alter_magias_savaguarda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magias',
            name='tipo_dado',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]