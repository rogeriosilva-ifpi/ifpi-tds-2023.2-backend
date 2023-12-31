# Generated by Django 4.2.6 on 2023-10-25 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_comprador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comprador',
            options={'verbose_name': 'Comprador', 'verbose_name_plural': 'Compradores'},
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('entrega', models.CharField(choices=[('retirada', 'RETIRADA'), ('delivery', 'DELIVERY')], max_length=100)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='core.comprador')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to='core.produto')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
