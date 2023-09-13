from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название тестирования')
    description = models.TextField(max_length=511, verbose_name='Описание')
    question = models.ManyToManyField('Question', blank=True, verbose_name='Вопросы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тестирование'
        verbose_name_plural = 'Тестирования'
        ordering = ['title']


class Question(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['question']


class Answer(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст ответа')
    is_true = models.BooleanField(default=False, verbose_name='Верный ответ')
    question = models.ForeignKey('Question', null=True, on_delete=models.PROTECT, verbose_name='Вопрос', related_name='answers')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['text']
