# Generated by Django 4.0.6 on 2022-07-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(max_length=512, primary_key=True, serialize=False),
        ),
    ]
