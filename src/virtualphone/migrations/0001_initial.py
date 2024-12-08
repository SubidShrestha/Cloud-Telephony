# Generated by Django 5.1.4 on 2024-12-08 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('usage', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='virtual_phone_numbers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Virtual Phone Number',
                'verbose_name_plural': 'Virtual Phone Numbers',
                'db_table': 'virtual_phone_numbers',
            },
        ),
        migrations.CreateModel(
            name='CallLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('call_type', models.CharField(choices=[('incoming', 'Incoming'), ('outgoing', 'Outgoing')], max_length=10)),
                ('duration', models.PositiveIntegerField()),
                ('virtual_phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='virtualphone.virtualphonenumber')),
            ],
            options={
                'verbose_name': 'Call Log',
                'verbose_name_plural': 'Call Logs',
                'db_table': 'call_logs',
            },
        ),
    ]