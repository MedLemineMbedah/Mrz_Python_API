# Generated by Django 4.0.3 on 2022-03-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadorimrest', '0007_backcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='none', max_length=100)),
                ('nationalite', models.CharField(default='none', max_length=100)),
            ],
        ),
    ]