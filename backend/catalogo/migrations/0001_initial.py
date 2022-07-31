# Generated by Django 4.0.6 on 2022-07-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(default=1000, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('medidas', models.CharField(max_length=15)),
                ('colores', models.CharField(max_length=20)),
                ('foto', models.FileField(null=True, upload_to='images/')),
            ],
            options={
                'ordering': ['stock'],
            },
        ),
    ]