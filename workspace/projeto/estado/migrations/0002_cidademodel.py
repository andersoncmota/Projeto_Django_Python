# Generated by Django 2.2 on 2019-06-05 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CidadeModel',
            fields=[
                ('cidade_id', models.AutoField(primary_key=True, serialize=False)),
                ('cidade_nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade_Nome')),
                ('cidade_ddd', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade_ddd')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estado.EstadoModel')),
            ],
        ),
    ]