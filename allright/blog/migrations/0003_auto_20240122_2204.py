# Generated by Django 5.0 on 2024-01-22 22:04

from django.db import migrations
from ..models import Case
def create_cases(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Case = apps.get_model('blog', 'Case')
    Case.objects.using(db_alias).create(
        titulo='Case_Teste',
        conteudo='Conteudo_Teste',
    )

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_case_post_data_publicacao_post_midia'),
    ]

    operations = [
        migrations.RunPython(create_cases),
    ]