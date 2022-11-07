# Generated by Django 4.1.3 on 2022-11-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familiares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('ID', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=40)),
                ('profesion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Familiar3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('ID', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=40)),
                ('profesion', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameModel(
            old_name='Familiar',
            new_name='Familiar1',
        ),
    ]
