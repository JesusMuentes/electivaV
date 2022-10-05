# Generated by Django 4.1.2 on 2022-10-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=100)),
                ('indi_carga', models.EmailField(max_length=254)),
                ('indi_velocidad', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
