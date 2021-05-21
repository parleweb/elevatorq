# Generated by Django 3.2.3 on 2021-05-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevatorq', '0005_auto_20210521_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingelevator',
            name='speed_close',
            field=models.DecimalField(decimal_places=1, default=3.7, help_text='in simili seconds, closing door', max_digits=3),
        ),
        migrations.AlterField(
            model_name='buildingelevator',
            name='speed_floor',
            field=models.DecimalField(decimal_places=1, default=2.1, help_text='in simili seconds, elevator travel one floor', max_digits=3),
        ),
        migrations.AlterField(
            model_name='buildingelevator',
            name='speed_open',
            field=models.DecimalField(decimal_places=1, default=8.4, help_text='in simili seconds, opening door + people goes out/in', max_digits=3),
        ),
    ]