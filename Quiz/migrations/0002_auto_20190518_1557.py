# Generated by Django 2.2.1 on 2019-05-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='full_marks',
        ),
    ]
