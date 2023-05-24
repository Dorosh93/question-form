from django import forms
from django.core.exceptions import ValidationError
from .models import Company, Division


def get_list_comp():
    list_comp = [('другое', 'другое')]
    comp = Company.objects.all()
    for i in comp:
        list_comp.append((i.title, i.title))
    return list_comp


def validate_email(еmail):
    if еmail[-3:] != '.ru':
        raise ValidationError('Введите почту из домена .ru')


class CompanyQuestionForm(forms.Form):
    division = forms.ModelChoiceField(
        widget=forms.Select(attrs={'id': 'id_form_division'}),
        queryset=Division.objects.all(),
        help_text='Выберите ваш дивизион'
        )
    company = forms.ChoiceField(
        widget=forms.Select(attrs={'id': 'id_form_company'}),
        choices=get_list_comp,
        help_text='Выберите ваше предприятие'
        )
    title = forms.CharField(max_length=200,
                            help_text='Название предприятия',
                            required=False,
                            widget=forms.TextInput(
                                attrs={'id': 'id_form_title'}
                                ),
                            )
    email = forms.EmailField(help_text=('Если вы хотите лично получить ответ '
                                        'на ваш вопрос, оставьте электронную '
                                        'почту, на которую необходимо отправить'
                                        ' ответ (можно не корпоративную)'
                                        ),
                             validators=[validate_email],
                             required=False
                             )

    text = forms.CharField(
        widget=forms.Textarea,
        help_text=('Задайте ваш вопрос генеральному директору '
                   'Госкорпорации "Росатом" А.Е. Лихачеву'
                   ),
        )
