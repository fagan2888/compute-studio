# Generated by Django 3.0.9 on 2020-08-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200824_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runningdeployment',
            name='ready',
        ),
        migrations.AddField(
            model_name='runningdeployment',
            name='status',
            field=models.CharField(choices=[('creating', 'Creating'), ('running', 'Running'), ('terminated', 'Terminated')], default='creating', max_length=32),
        ),
    ]
