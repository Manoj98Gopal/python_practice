# Generated by Django 5.0.3 on 2024-03-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='00000', max_length=20),
            preserve_default=False,
        ),
    ]
