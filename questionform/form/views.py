from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Question, Division
from .forms import CompanyQuestionForm


@csrf_exempt
def question_create(request):
    form_cq = CompanyQuestionForm(request.POST or None)
    if request.method == 'POST':
        valid = form_cq.is_valid()
        choice_comp = form_cq.cleaned_data['company']
        if valid:
            if choice_comp == 'другое':
                comp = Company(
                    title=form_cq.cleaned_data['title'],
                    division=form_cq.cleaned_data['division']
                    )
                comp.save()
                Question(company=comp, email=form_cq.cleaned_data['email'],
                         text=form_cq.cleaned_data['text']
                         ).save()
            else:
                compan = get_object_or_404(Company, title=form_cq.cleaned_data['company'])
                Question(company=compan,
                         email=form_cq.cleaned_data['email'],
                         text=form_cq.cleaned_data['text']
                         ).save()
            return redirect(request.get_full_path())
    else:
        choice_comp = ''
    dict_div_comp = {}
    divis = Division.objects.all()
    comp = Company.objects.all()
    for i in divis:
        dict_div_comp[i.title] = []
    for j in comp:
        dict_div_comp[j.division.title].append(j.title)
    context = {
        'choice_comp': choice_comp,
        'dict_div_comp': dict_div_comp,
        'form_cq': form_cq
    }
    return render(request, 'question_form.html', context)
