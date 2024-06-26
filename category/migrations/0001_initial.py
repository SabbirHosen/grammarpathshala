# Generated by Django 4.0.5 on 2022-06-09 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='category.node')),
            ],
            options={
                'verbose_name_plural': 'Nodes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('category.node',),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('category.node',),
        ),
    ]
