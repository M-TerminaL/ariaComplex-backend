# Generated by Django 3.2.25 on 2024-07-31 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_module', '0010_remove_services_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablepricesrows',
            name='discount_price',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True, verbose_name='قیمت با تخفیف'),
        ),
    ]
