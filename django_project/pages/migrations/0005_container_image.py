# Generated by Django 4.0.6 on 2022-08-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_container_registry_pro_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registry_name', models.CharField(max_length=512)),
                ('image', models.CharField(max_length=512)),
                ('size', models.FloatField()),
            ],
        ),
    ]
