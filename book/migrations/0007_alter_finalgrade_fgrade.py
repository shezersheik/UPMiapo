# Generated by Django 4.0.4 on 2022-04-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_remove_grade_subject_remove_lesson_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalgrade',
            name='fgrade',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('ЗЧ', 'Зачет'), ('НЗ', 'Не зачет')], max_length=2, null=True, verbose_name='Оценка'),
        ),
    ]
