# Generated by Django 5.0 on 2024-01-28 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('introducao', models.TextField(blank=True, null=True, verbose_name='Introdução')),
                ('trabalho_executado', models.TextField(verbose_name='Trabalho executado')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Mídia')),
                ('data_publicacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de publicação')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('case_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.case')),
            ],
            bases=('blog.case',),
        ),
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255)),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.case')),
            ],
        ),
    ]
