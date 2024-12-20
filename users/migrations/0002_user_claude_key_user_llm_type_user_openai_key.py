# Generated by Django 5.1.2 on 2024-10-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='claude_key',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='llm_type',
            field=models.CharField(choices=[('openai', 'Open AI'), ('claude', 'Claude')], default='openai', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='openai_key',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
