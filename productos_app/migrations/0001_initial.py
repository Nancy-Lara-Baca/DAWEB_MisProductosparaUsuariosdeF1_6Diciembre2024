# Generated by Django 5.1.3 on 2024-12-03 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id_producto', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad_productos', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]