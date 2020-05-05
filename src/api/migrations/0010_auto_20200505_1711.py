# Generated by Django 2.2.10 on 2020-05-05 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_successstory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='successstory',
            options={'verbose_name_plural': 'Success Stories'},
        ),
        migrations.AlterField(
            model_name='successstory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='successstory',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
