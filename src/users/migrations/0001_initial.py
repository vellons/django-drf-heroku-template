# Generated by Django 4.0.3 on 2022-03-17 23:21

import django.core.validators
from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 32 characters or fewer. Lowercase letters, digits _ only; must start with a letter.', max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(4), users.validators.MyUsernameValidator()])),
                ('name', models.CharField(max_length=64, null=True)),
                ('surname', models.CharField(max_length=64, null=True)),
                ('type', models.CharField(choices=[('STD', 'Standard'), ('ADM', 'Admin')], default='STD', max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
