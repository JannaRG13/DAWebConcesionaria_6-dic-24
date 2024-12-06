# Generated by Django 5.1.2 on 2024-12-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('precio', models.IntegerField()),
                ('forma_pago', models.CharField(max_length=255)),
                ('id_vehiculo', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
                ('id_empleado', models.IntegerField()),
            ],
        ),
    ]
