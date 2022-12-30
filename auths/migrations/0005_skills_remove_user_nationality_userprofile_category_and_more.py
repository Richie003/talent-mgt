# Generated by Django 4.0 on 2022-12-27 01:40

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0004_alter_user_tel_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, default='', max_length=123)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='nationality',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.CharField(blank=True, choices=[('Closer', 'Closer'), ('Appointment_setter', 'Appointment_setter')], default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cover_letter',
            field=djrichtextfield.models.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.CharField(blank=True, default='', max_length=9),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nationality',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(default='', upload_to='resumes /% Y % m % d/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_type',
            field=models.CharField(blank=True, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(to='auths.Skills'),
        ),
    ]