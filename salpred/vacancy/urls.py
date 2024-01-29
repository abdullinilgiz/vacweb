from django.urls import path

from vacancy.views import list_vacancies, create_vacancy

app_name = 'vacancy'

urlpatterns = [
    path('', list_vacancies, name='list_vacancies'),
    path('create/', create_vacancy, name='create_vacancy'),
    # path('<int: vacancy_id>/', get_vacancy),
]
