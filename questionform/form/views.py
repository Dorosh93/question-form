import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Question, Division
from .forms import CompanyQuestionForm


@csrf_exempt
def question_create(request):
    form_question = CompanyQuestionForm(request.POST or None)
    chosen_comp = ''
    if request.method == 'POST':
        valid = form_question.is_valid()
        # print(form_question)
        chosen_comp = form_question.cleaned_data['company']
        if valid:
            title_form = form_question.cleaned_data['title']
            division_form = form_question.cleaned_data['division']
            if (chosen_comp == 'другое' and Company.objects.filter(
                 division=division_form, title=title_form).exists() == False):
                # проверка, что вводимой компании нет в выпадающем списке
                compan = Company(
                    title=title_form,
                    division=division_form
                    )
                compan.save()
            else:
                if chosen_comp != 'другое':
                    title_form = chosen_comp
                compan = get_object_or_404(
                    Company,
                    division=division_form,
                    title=title_form
                    )
            Question(company=compan,
                     email=form_question.cleaned_data['email'],
                     text=form_question.cleaned_data['text']
                     ).save()
            return redirect(request.get_full_path())

    division_to_companies = {}
    divisions = Division.objects.prefetch_related('companies').all()
    for division in divisions:
        division_to_companies[division.title] = []
        for company in division.companies.all():
            division_to_companies[division.title].append(company.title)
    context = {
        'chosen_comp': chosen_comp,
        'division_to_companies': json.dumps(division_to_companies),
        'form_question': form_question
    }
    return render(request, 'question_form.html', context)

def result_table(request):
    questions_from_companies = []
    questions = Question.objects.all()
    for question in questions:
        questions_from_companies.append([
            question.pub_date,
            str(question.company),
            question.text,
            question.email
        ])
    count_questions_conpany = []
    companies = Company.objects.prefetch_related('questions').all()
    for company in companies:
        count_questions_conpany.append([
            str(company.division),
            company.title,
            len(company.questions.all())
        ])
    return render(request,
                  'result_table.html',
                  {
                      'questions_from_companies': questions_from_companies,
                      'count_questions_conpany': count_questions_conpany
                      }
                  )
