# Generated by Django 4.0.5 on 2022-08-07 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_quiz_sub_category_remove_quiz_title_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizset',
            old_name='title_id',
            new_name='post_title',
        ),
    ]
