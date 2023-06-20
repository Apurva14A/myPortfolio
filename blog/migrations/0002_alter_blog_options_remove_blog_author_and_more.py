# Generated by Django 4.2.2 on 2023-06-19 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='status',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]