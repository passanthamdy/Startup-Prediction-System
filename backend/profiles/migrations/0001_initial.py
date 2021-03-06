# Generated by Django 3.2.4 on 2021-06-16 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=125, null=True, region=None, unique=True)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('about', models.TextField(blank=True, max_length=500)),
                ('avatar', models.ImageField(default='def.png', upload_to=profiles.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
