# Generated by Django 5.0.4 on 2024-05-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone_No', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Addres', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Course', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
