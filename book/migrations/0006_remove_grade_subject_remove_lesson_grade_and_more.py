# Generated by Django 4.0.4 on 2022-04-22 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_remove_grade_date_gr_remove_grade_fgrade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='grade',
        ),
        migrations.AddField(
            model_name='grade',
            name='lesson_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.lesson', verbose_name='Тема урока'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='homework',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Домашнее задание'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.subject', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='finalgrade',
            name='fgrade',
            field=models.CharField(choices=[('2', 'Не удовлетворительно'), ('3', 'Удовлетворительно'), ('4', 'Хорошо'), ('5', 'Отлично'), ('ЗЧ', 'Зачет'), ('НЗ', 'Не зачет')], max_length=2, null=True, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='finalgrade',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.student', verbose_name='Ученик'),
        ),
        migrations.AlterField(
            model_name='finalgrade',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.subject', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(choices=[('2', 'Не удовлетворительно'), ('3', 'Удовлетворительно'), ('4', 'Хорошо'), ('5', 'Отлично')], max_length=1, null=True, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.student', verbose_name='Ученик'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.teacher', verbose_name='Учитель'),
        ),
    ]
