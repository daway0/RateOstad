# Generated by Django 3.2 on 2022-11-21 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='constvalue',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Rate.constvalue', verbose_name='مقدار ثابت پدر'),
        ),
    ]
