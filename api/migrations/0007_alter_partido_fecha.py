# Generated by Django 5.0.3 on 2024-03-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_partido_hora_remove_partido_minuto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
