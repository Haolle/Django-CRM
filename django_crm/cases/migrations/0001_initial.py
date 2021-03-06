# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-08 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('case_type', models.CharField(blank=True, choices=[('Question', 'Question'), ('Incident', 'Incident'), ('Problem', 'Problem')], default='', max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('New', 'New'), ('Assigned', 'Assigned'), ('Pending', 'Pending'), ('Closed', 'Closed'), ('Rejected', 'Rejected'), ('Duplicate', 'Duplicate')], default='', max_length=64, null=True)),
                ('priority', models.CharField(blank=True, choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High'), ('Urgent', 'Urgent')], default='', max_length=64, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('teams', models.CharField(blank=True, choices=[('Sales', 'Sales'), ('Support', 'Support'), ('TopManagement', 'TopManagement')], default='', max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('assigned_user', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('account', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.LeadAccount')),
                ('contacts', models.ManyToManyField(blank=True, to='contacts.Contact')),
                ('userid', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('comment_file', models.FileField(default='', upload_to='media/comment_files', verbose_name='File')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('caseid', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='cases.Case')),
                ('comment_user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment_files',
            name='comment_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cases.Comments'),
        ),
    ]
