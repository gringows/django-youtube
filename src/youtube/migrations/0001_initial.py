# Generated by Django 3.0.8 on 2020-07-20 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='videos/uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.Video')),
            ],
        ),
    ]
