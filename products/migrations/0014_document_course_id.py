# Generated by Django 2.0.4 on 2018-04-28 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_fuckoff'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='course_id',
            field=models.ForeignKey(blank=True, default=850, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
