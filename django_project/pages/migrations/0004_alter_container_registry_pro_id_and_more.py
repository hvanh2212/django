# Generated by Django 4.0.6 on 2022-07-31 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_container_registry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container_registry',
            name='pro_id',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='container_registry',
            name='registry_name',
            field=models.CharField(max_length=512, primary_key=True, serialize=False),
        ),
    ]
