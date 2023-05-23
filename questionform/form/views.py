import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Question, Division
from .forms import CompanyQuestionForm


@csrf_exempt
def question_create(request):
    form_question = CompanyQuestionForm(request.POST or None)
    chosen_comp = ''  # проверить None
    if request.method == 'POST':
        valid = form_question.is_valid()
        chosen_comp = form_question.cleaned_data['company']
        if valid:
            if chosen_comp == 'другое':
                compan = Company(
                    title=form_question.cleaned_data['title'],
                    division=form_question.cleaned_data['division']
                    )
                compan.save()
            else:
                compan = get_object_or_404(
                    Company,
                    title=form_question.cleaned_data['company']
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
