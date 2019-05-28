# Generated by Django 2.2.1 on 2019-05-16 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=150)),
                ('date_of_birth', models.DateField(help_text="'YYYY-MM-DD' format")),
                ('specialised_subject', models.TextField()),
                ('previous_work_expreience', models.TextField()),
                ('working_as', models.TextField()),
                ('display_picture', models.URLField(blank=True, max_length=400)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('joining_time', models.TimeField(auto_now_add=True)),
                ('contact_number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('alternate_number', models.DecimalField(blank=True, decimal_places=0, max_digits=10)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('date_of_birth', models.DateField(help_text="Should be in 'YYYY-MM-DD' format")),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=50)),
                ('contact_number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('address', models.TextField()),
                ('display_picture', models.URLField(blank=True, max_length=400)),
                ('name_of_father', models.CharField(blank=True, max_length=200)),
                ('name_of_mother', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]