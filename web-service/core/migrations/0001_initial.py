# Generated by Django 2.1.2 on 2019-10-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('primary_key', models.AutoField(primary_key=True, serialize=False)),
                ('headers', models.TextField()),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
