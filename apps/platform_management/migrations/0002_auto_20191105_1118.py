# Generated by Django 2.0.6 on 2019-11-05 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('platform_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformuserinfo',
            name='update_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platform_update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AddField(
            model_name='platformuserinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pu_user', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]