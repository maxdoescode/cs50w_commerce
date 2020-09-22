# Generated by Django 3.1.1 on 2020-09-22 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='placedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='placedTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placedTo', to='auctions.listing'),
        ),
    ]
