# Generated by Django 4.1.7 on 2023-06-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "ApiArriendosAlegria",
            "0006_remove_propiedad_externo_propiedad_observaciones_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="detallearriendo",
            name="toca_reajuste",
            field=models.BooleanField(default=False),
        ),
    ]
