# Generated by Django 4.2.5 on 2023-09-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_api', '0002_note_user_id_alter_note_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]