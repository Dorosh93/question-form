# Generated by Django 3.2.19 on 2023-05-22 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20230521_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('title',)},
        ),
        migrations.AlterField(
            model_name='question',
            name='company',
            field=models.ForeignKey(help_text='Выберите ваше предприятие', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='form.company', verbose_name='Предприятие'),
        ),
    ]
