# Generated by Django 5.1 on 2024-12-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id_producto',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
