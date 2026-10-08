from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('entregas', '0001_initial')]

    operations = [
        migrations.AddField(model_name='pedido', name='medio', field=models.CharField(blank=True, default='', max_length=20)),
        migrations.AddField(model_name='pedido', name='detalle_plan', field=models.CharField(blank=True, default='', max_length=100)),
        migrations.AddField(model_name='pedido', name='horas_estimadas', field=models.PositiveSmallIntegerField(default=2)),
    ]
