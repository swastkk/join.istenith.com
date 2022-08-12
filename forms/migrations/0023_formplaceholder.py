# Generated by Django 4.0.6 on 2022-08-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0022_template_success_message_alter_registeration_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormPlaceholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_input', models.CharField(max_length=100)),
                ('email_input', models.CharField(max_length=100)),
                ('phone_number_input', models.CharField(max_length=100)),
                ('cv_upload_input', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Form Placeholder',
                'verbose_name_plural': 'Form Placeholders',
            },
        ),
    ]