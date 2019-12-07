# Generated by Django 2.2.4 on 2019-11-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctorModel',
            fields=[
                ('doc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('specialization', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]