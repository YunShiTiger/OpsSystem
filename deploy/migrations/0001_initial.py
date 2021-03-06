# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-12 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeployInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repoName', models.CharField(max_length=100)),
                ('target', models.CharField(max_length=10)),
                ('revision', models.CharField(max_length=100)),
                ('person', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('remark', models.CharField(default=None, max_length=80)),
                ('log', models.TextField()),
            ],
            options={
                'db_table': 'ops_deploy_info',
            },
        ),
        migrations.CreateModel(
            name='RepoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repoName', models.CharField(max_length=100)),
                ('repoAddress', models.CharField(max_length=100)),
                ('repoUser', models.CharField(max_length=50)),
                ('repoPassword', models.CharField(blank=True, max_length=50)),
                ('wwwDir', models.CharField(max_length=50)),
                ('testDeployIP', models.CharField(max_length=50)),
                ('preDeployIP', models.CharField(max_length=50)),
                ('onlineDeployIP', models.CharField(max_length=500)),
                ('localCheckoutDir', models.CharField(max_length=100)),
                ('excludeDir', models.CharField(max_length=500)),
                ('repoType', models.CharField(choices=[('svn', 'svn repo type'), ('git', 'git repo type')], max_length=5)),
                ('addDate', models.DateTimeField()),
            ],
            options={
                'db_table': 'ops_repo_info',
            },
        ),
        migrations.CreateModel(
            name='RollBackInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repoName', models.CharField(max_length=100)),
                ('curRevision', models.CharField(max_length=30)),
                ('backRevision', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('success', 'rollback success'), ('failed', 'rollback failed')], max_length=10)),
                ('rollDate', models.DateTimeField()),
                ('target', models.CharField(max_length=10)),
                ('person', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'ops_rollback_info',
            },
        ),
    ]
