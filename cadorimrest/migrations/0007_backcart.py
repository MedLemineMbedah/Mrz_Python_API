# Generated by Django 4.0.3 on 2022-03-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadorimrest', '0006_frcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateEmission', models.CharField(default='none', max_length=100)),
                ('dateValidie', models.CharField(default='none', max_length=100)),
                ('Path', models.CharField(default='none', max_length=100)),
            ],
        ),
    ]
