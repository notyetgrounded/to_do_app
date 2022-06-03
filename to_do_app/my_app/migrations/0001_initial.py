# Generated by Django 4.0.3 on 2022-06-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeStamp', models.DateTimeField()),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=1000)),
                ('DueDate', models.DateField()),
                ('Tag', models.CharField(max_length=10)),
                ('Status', models.CharField(default='OPEN', max_length=10)),
            ],
        ),
    ]
