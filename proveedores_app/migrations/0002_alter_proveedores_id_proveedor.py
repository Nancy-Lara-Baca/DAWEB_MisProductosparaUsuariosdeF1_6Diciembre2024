# Generated by Django 5.1 on 2024-12-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='id_proveedor',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]