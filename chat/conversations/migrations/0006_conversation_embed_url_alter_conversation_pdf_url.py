# Generated by Django 5.1.2 on 2024-10-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_conversations', '0005_alter_conversation_last_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='embed_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='pdf_url',
            field=models.TextField(blank=True),
        ),
    ]