# Generated by Django 5.1 on 2024-12-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores_app', '0002_alter_proveedores_id_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='id_proveedor',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]