# Generated by Django 5.1.2 on 2024-10-21 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_messages', '0003_alter_message_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='type',
            new_name='role',
        ),
    ]
