# Generated by Django 5.1.1 on 2024-09-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='post_img')),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
            ],
        ),
    ]