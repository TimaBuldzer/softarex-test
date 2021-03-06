# Generated by Django 4.0.5 on 2022-06-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ImageField(upload_to='cases/original/%Y/%m/%d')),
                ('encoded', models.ImageField(upload_to='cases/encoded/%Y/%m/%d')),
            ],
        ),
    ]
