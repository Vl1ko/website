# Generated by Django 4.2 on 2023-04-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_response_order_phone_response_age_r_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='tel_r',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Теле Аниматора'),
        ),
    ]