# Generated by Django 5.0.6 on 2024-05-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_actor_main_picture_director_main_picture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotbal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
