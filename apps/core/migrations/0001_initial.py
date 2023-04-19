# Generated by Django 4.2 on 2023-04-15 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('CARBOHIDRATO', 'carbohidratos'), ('GRASA', 'grasas'), ('PROTEINA', 'proteina')], max_length=200)),
                ('calorias', models.IntegerField(help_text='por cada 100g')),
                ('proteina', models.IntegerField(help_text='por cada 100g')),
            ],
        ),
        migrations.CreateModel(
            name='Reseta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cycle', models.CharField(choices=[('DESAYUNO', 'desayuno'), ('MERIENDA', 'merienda'), ('ALMUERZO', 'almuerzo'), ('CENA', 'cena')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.food')),
            ],
        ),
        migrations.CreateModel(
            name='CantidadesReseta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.food')),
                ('reseta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.reseta')),
            ],
        ),
    ]