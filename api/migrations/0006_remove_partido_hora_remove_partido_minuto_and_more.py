# Generated by Django 5.0.3 on 2024-03-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_partido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partido',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='minuto',
        ),
        migrations.AlterField(
            model_name='partido',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]