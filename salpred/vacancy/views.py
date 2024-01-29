from django.shortcuts import render, redirect
from vacancy.models import Vacancy
from vacancy.forms import VacancyForm




def create_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            # salary = get_salary(position, education, region, exp, skills, schedule)
            form.save()
            return redirect('vacancy:list_vacancies')
    else:
        form = VacancyForm()
    return render(request, 'vacancy/create.html', {'form': form})


def list_vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy/list.html', {'vacancies': vacancies})
