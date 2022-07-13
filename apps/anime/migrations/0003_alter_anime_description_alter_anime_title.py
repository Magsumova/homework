# Generated by Django 4.0 on 2022-05-03 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_genre_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.description', verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='title',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.title', verbose_name='название'),
        ),
    ]