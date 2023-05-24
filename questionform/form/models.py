from django.db import models


class Division(models.Model):
    title = models.CharField(
        'Название дивизиона',
        unique=True,
        max_length=200,
        help_text='Название дивизиона'
    )

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(
        'Название предприятия',
        unique=True,
        max_length=200,
        help_text='Название предприятия'
    )
    division = models.ForeignKey(
        Division,
        on_delete=models.PROTECT,
        verbose_name='Дивизион',
        related_name='companies',
        help_text='Выберите ваш дивизион'
    )

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(
        'Текст вопроса',
        help_text='Текст вопроса'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Предприятие',
        related_name='questions',
        help_text='Выберите ваше предприятие'
    )
    pub_date = models.DateTimeField(
        'Дата и время создания вопроса',
        auto_now_add=True,
        help_text='Дата и время создания вопроса'
    )
    email = models.EmailField(
        max_length=254,
        unique=False,
        blank=True,
        null=True,
        verbose_name='E-mail',
        help_text='E-mail'
    )

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:15]
