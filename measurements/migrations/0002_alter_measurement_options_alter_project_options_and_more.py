# Generated by Django 4.2.1 on 2023-08-01 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['-created_at'], 'verbose_name': 'Замер', 'verbose_name_plural': 'Замеры'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id'], 'verbose_name': 'Термодатчик', 'verbose_name_plural': 'Термодатчики'},
        ),
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurements.project'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='value',
            field=models.FloatField(verbose_name='Температура'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
