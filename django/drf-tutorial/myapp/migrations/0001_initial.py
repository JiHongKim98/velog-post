# Generated by Django 4.2.5 on 2023-10-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charFields1', models.CharField(default='hi1', max_length=10)),
                ('charFields2', models.CharField(default='hi2', max_length=20)),
                ('content', models.TextField()),
            ],
        ),
    ]
