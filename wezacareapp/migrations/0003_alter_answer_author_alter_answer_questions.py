# Generated by Django 4.1.7 on 2023-03-21 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wezacareapp', '0002_alter_questions_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer', to='wezacareapp.questions'),
        ),
    ]