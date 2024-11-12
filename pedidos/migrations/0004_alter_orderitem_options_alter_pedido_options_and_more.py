# Generated by Django 5.0.6 on 2024-06-25 18:49

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_pedido_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['id'], 'verbose_name': 'Orden de Compra', 'verbose_name_plural': 'Ordenes de Compra'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['id'], 'verbose_name': 'pedido', 'verbose_name_plural': 'pedidos'},
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='Producto',
            new_name='producto',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='Pedido',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='precio',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='crear_en',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='pedido_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterModelTable(
            name='orderitem',
            table='orden_de_compra',
        ),
        migrations.AlterModelTable(
            name='pedido',
            table='pedidos',
        ),
    ]