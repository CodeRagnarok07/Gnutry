# Generated by Django 4.2 on 2023-04-23 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alimentos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cycle', models.CharField(choices=[('DESAYUNO', 'desayuno'), ('MERIENDA', 'merienda'), ('ALMUERZO', 'almuerzo'), ('CENA', 'cena')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CantidadesReseta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alimentos.food')),
                ('reseta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.reseta')),
            ],
        ),
    ]
