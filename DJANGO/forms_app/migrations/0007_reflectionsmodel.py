# Generated by Django 2.1.2 on 2018-10-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0006_auto_20181017_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReflectionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=500)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
