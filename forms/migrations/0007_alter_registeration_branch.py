# Generated by Django 4.0.5 on 2022-06-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_alter_registeration_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='branch',
            field=models.PositiveIntegerField(choices=[
                (1, 'Civil Engineering'), (2, 'Mechanical Engineering'),
                (3, 'Electrical Engineering'),
                (4, 'Elctronics And Communication Engineering'),
                (5, 'Chemical Engineering'),
                (6, 'Computer Science Engineering'), (7, 'Material Science'),
                (8, 'Engineering Physics'), (9, 'Mathematics And Computing')
            ],
                                              default='Select Your Branch'),
        ),
    ]
