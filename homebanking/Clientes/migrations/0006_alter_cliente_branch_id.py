# Generated by Django 4.1 on 2022-09-07 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursales', '0004_remove_sucursal_loan_id'),
        ('Clientes', '0005_remove_direccioncliente_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='branch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Sucursales.sucursal'),
        ),
    ]