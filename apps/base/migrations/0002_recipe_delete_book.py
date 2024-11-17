# Generated by Django 5.1.3 on 2024-11-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('prep_time', models.IntegerField(default=1)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
