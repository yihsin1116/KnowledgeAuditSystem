# Generated by Django 3.0 on 2019-12-03 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('userid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100)),
                ('career_name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
