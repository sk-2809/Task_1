# Generated by Django 3.0.7 on 2020-06-22 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSP', '0003_auto_20200622_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itsp',
            name='Team_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
