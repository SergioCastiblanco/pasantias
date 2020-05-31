# Generated by Django 3.0.5 on 2020-04-23 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pasantias', '0007_remove_empresa_facultad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='pasantias.Empresa'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='pasantias.Usuario'),
        ),
    ]