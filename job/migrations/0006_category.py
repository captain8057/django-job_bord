# Generated by Django 3.1.1 on 2020-09-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200925_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
            ],
        ),
    ]