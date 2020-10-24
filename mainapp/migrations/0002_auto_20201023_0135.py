# Generated by Django 3.1.2 on 2020-10-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='box_amount',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='box',
            name='box_pay',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='box',
            name='box_size',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='box',
            name='box_value',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='box',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='box_latest',
            field=models.BooleanField(default=True),
        ),
    ]