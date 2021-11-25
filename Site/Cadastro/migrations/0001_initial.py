# Generated by Django 3.2.6 on 2021-11-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.CharField(max_length=200)),
                ('sexo', models.CharField(choices=[('M', 'Masxulino'), ('F', 'Feminino')], max_length=20)),
            ],
        ),
    ]
