# Generated by Django 2.2.3 on 2019-07-31 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0004_auto_20190731_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessemployee',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_1', to='Business.Business'),
        ),
        migrations.AlterField(
            model_name='businessemployee',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_1', to='Business.Employee'),
        ),
    ]
