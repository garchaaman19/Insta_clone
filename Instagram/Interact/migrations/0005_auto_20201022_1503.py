# Generated by Django 3.1.2 on 2020-10-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interact', '0004_auto_20201022_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='followers', to='Interact.Profile'),
        ),
    ]
