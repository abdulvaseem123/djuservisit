# Generated by Django 3.0.8 on 2020-07-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uservisitdashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservisit',
            name='doc_attached',
            field=models.BooleanField(default=False),
        ),
    ]
