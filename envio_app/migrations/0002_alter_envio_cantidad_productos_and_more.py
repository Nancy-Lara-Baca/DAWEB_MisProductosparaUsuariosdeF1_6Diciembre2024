# Generated by Django 5.1 on 2024-12-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='cantidad_productos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='envio',
            name='id_cliente',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='envio',
            name='id_empleado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='envio',
            name='id_envio',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='envio',
            name='id_producto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='envio',
            name='total',
            field=models.IntegerField(),
        ),
    ]
