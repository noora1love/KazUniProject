import datetime

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .templatetags.appay_tags import get_items_from_db
from .models import ModelPays, TableModelPays, budgetitems, projects, countrypartyes, deals, typeofoperations, typeofpays, organizations, bankcards, RegPay
from django.views.generic import DetailView, UpdateView
from django.views.decorators.http import require_POST
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.urls import reverse_lazy
import json
from .serializers import ModelPaysSerializer


def get_model_pay_data(request, record_id):
    model_pay = get_object_or_404(ModelPays, id=record_id)

    data = {
        'id': model_pay.id,
        'title': model_pay.title.strip(),
        'comments': model_pay.comments.strip(),
        'typeofoperation_name': model_pay.typeofoperation.name.strip(),
        'typeofpay_name': model_pay.typeofpay.name.strip(),
        'organization_name': model_pay.organization.name.strip(),
        'bankcard_name': model_pay.bankcard.name.strip(),
        'countrparty_name': model_pay.countrparty.name.strip(),
        'dateofstart': model_pay.dateofstart.isoformat() if model_pay.dateofstart is not None else '',
        'dateofend': model_pay.dateofend.isoformat() if model_pay.dateofend else '',
    }

    field_names = ['typeofoperations', 'typeofpays', 'organizations', 'bankcards', 'countrypartyes']
    field_data = {field_name: get_items_from_db(field_name) for field_name in field_names}

    label_texts = {
        'typeofoperations': 'Тип операции',
        'typeofpays': 'Тип оплаты',
        'organizations': 'Организация',
        'bankcards': 'Банковская карта',
        'countrypartyes': 'Контрагент',
    }

    if request.method == 'POST':
        title = request.POST.get('title').strip()
        typeofoperations_name = request.POST.get('typeofoperations_name').strip()
        typeofpays_name = request.POST.get('typeofpays_name').strip()
        organizations_name = request.POST.get('organizations_name').strip()
        bankcards_name = request.POST.get('bankcards_name').strip()
        countrypartyes_name = request.POST.get('countrypartyes_name').strip()
        dateofstart = request.POST.get('dateofstart').strip()
        dateofend = request.POST.get('dateofend').strip()
        comments = request.POST.get('comments').strip()

        typeofoperation_instance = get_object_or_404(typeofoperations, name=typeofoperations_name)
        typeofpay_instance = get_object_or_404(typeofpays, name=typeofpays_name)
        organization_instance = get_object_or_404(organizations, name=organizations_name)
        bankcard_instance = get_object_or_404(bankcards, name=bankcards_name)

        print(f'Trying to get countrypartyes with name: {countrypartyes_name}')
        countryparty_instance = get_object_or_404(countrypartyes.objects.all(), name=countrypartyes_name)

        model_pay = get_object_or_404(ModelPays, id=record_id)

        model_pay.title = title
        model_pay.typeofoperation = typeofoperation_instance
        model_pay.typeofpay = typeofpay_instance
        model_pay.organization = organization_instance
        model_pay.bankcard = bankcard_instance
        model_pay.countrparty = countryparty_instance

        # Преобразование строк в объекты datetime или None, если строка пуста
        model_pay.dateofstart = datetime.datetime.strptime(dateofstart, '%Y-%m-%d').date() if dateofstart else None
        model_pay.dateofend = datetime.datetime.strptime(dateofend, '%Y-%m-%d').date() if dateofend else None
        model_pay.comments = comments

        model_pay.save()

        return redirect('appay_main')

    return render(request, 'appay/updateform.html', {'data': data,'field_data': field_data, 'field_names': field_names, 'label_texts': label_texts})


class NewsUpdateView(UpdateView):
    model = ModelPays
    template_name = 'appay/updateform.html'

    fields = ['title','typeofoperation', 'typeofpay', 'organization', 'bankcard', 'countrparty', 'dateofstart', 'dateofend']
    success_url = reverse_lazy('appay_main')

class CountrypartyDetailView(DetailView):
    model = countrypartyes
    template_name = 'appay/countryparty.html'  # Создайте новый шаблон для детального просмотра
    context_object_name = 'countryparty'

class DealDetailView(DetailView):
    model = deals
    template_name = 'appay/deals.html'  # Создайте новый шаблон для детального просмотра
    context_object_name = 'deals'


def appay_countryparty(request):
    countryparty = countrypartyes.objects.all()
    return render(request, 'appay/countryparty.html', {'countryparty': countryparty})
def appay_home(request):
    modelpays = ModelPays.objects.all()
    return render(request, 'appay/appay.html', {'modelpays': modelpays})

class DataListView(View):
    def get(self, request, model_name, *args, **kwargs):
        models = {
            'typeofoperations': typeofoperations,
            'typeofpays': typeofpays,
            'organizations': organizations,
            'bankcards': bankcards,
            'countrypartyes': countrypartyes,
            'dealofcountrparty': deals,
            'budgetitem' :  budgetitems,
            'project' : projects
        }

        model = models.get(model_name)
        if not model:
            return JsonResponse({'error': 'Invalid model name'}, status=400)

        data = list(model.objects.values())
        return JsonResponse(data, safe=False)


def profile(request):
    return render(request, 'appay/profile.html')


class NewsDetailView(DetailView):
    model = ModelPays
    template_name = 'appay/form.html'
    context_object_name = 'modelpay'




@require_POST
def delete_selected(request):
    selected_ids = request.POST.getlist('delete')

    if selected_ids:
        ModelPays.objects.filter(id__in=selected_ids).delete()

    return redirect('appay_main')

@require_POST
def delete_selected_RegPay(request):
    selected_ids = request.POST.getlist('delete')

    if selected_ids:
        RegPay.objects.filter(id__in=selected_ids).delete()

    return redirect('RegPay')
def your_table_view(request):

        # Если запрос не POST, отображаем страницу с таблицей
        field_names = ['typeofoperations', 'typeofpays', 'organizations', 'bankcards', 'countrypartyes']
        field_data = {field_name: get_items_from_db(field_name) for field_name in field_names}
        label_texts = {
            'typeofoperations': 'Тип операции',
            'typeofpays': 'Тип оплаты',
            'organizations': 'Организация',
            'bankcards': 'Банковская карта',
            'countrypartyes': 'Контрагент',
        }
        # Отображаем страницу с таблицей
        return render(request, 'appay/test.html', {'field_data': field_data, 'field_names': field_names, 'label_texts': label_texts})


def appay_createform(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса для ModelPays
        title = request.POST.get('title')
        typeofoperations_name = request.POST.get('typeofoperations_name')
        typeofpays_name = request.POST.get('typeofpays_name')
        organizations_name = request.POST.get('organizations_name')
        bankcards_name = request.POST.get('bankcards_name')
        countrypartyes_name = request.POST.get('countrypartyes_name')
        dateofstart = request.POST.get('dateofstart')
        dateofend = request.POST.get('dateofend')
        comments = request.POST.get('comments')

        # Получаем объекты из базы данных для ModelPays
        typeofoperation_instance = get_object_or_404(typeofoperations, name=typeofoperations_name)
        typeofpay_instance = get_object_or_404(typeofpays, name=typeofpays_name)
        organization_instance = get_object_or_404(organizations, name=organizations_name)
        bankcard_instance = get_object_or_404(bankcards, name=bankcards_name)
        countryparty_instance = get_object_or_404(countrypartyes, name=countrypartyes_name)

        # Создаем новый объект ModelPays
        new_model_pays = ModelPays(
            title=title,
            typeofoperation=typeofoperation_instance,
            typeofpay=typeofpay_instance,
            organization=organization_instance,
            bankcard=bankcard_instance,
            countrparty=countryparty_instance,
            dateofstart=dateofstart,
            dateofend=dateofend,
            comments=comments
        )
        new_model_pays.save()

        # Получаем данные из POST-запроса для TableModelPays
        numberofline = request.POST.get('numberofline')
        dealofcountrparty_name = request.POST.get('dealofcountrparty_name')
        paymentamount_name = request.POST.get('paymentamount_name')
        budgetitem_name = request.POST.get('budgetitem_name')
        project_name = request.POST.get('project_name')

        # Получаем объекты из базы данных для TableModelPays
        dealofcountrparty_instance = get_object_or_404(deals, name=dealofcountrparty_name)
        budgetitem_instance = get_object_or_404(budgetitems, name=budgetitem_name)
        project_instance = get_object_or_404(projects, name=project_name)

        # Создаем новый объект TableModelPays
        new_table_model_pays = TableModelPays(
            numberofline=numberofline,
            dealofcountrparty=dealofcountrparty_instance,
            paymentamount=paymentamount_name,
            budgetitem=budgetitem_instance,
            project=project_instance
        )
        new_table_model_pays.save()

        # Перенаправляем пользователя на другую страницу после успешного создания объектов
        return redirect('appay_main')

    else:
        # Логика для GET-запроса

        field_names = ['typeofoperations', 'typeofpays', 'organizations', 'bankcards', 'countrypartyes']
        field_data = {field_name: get_items_from_db(field_name) for field_name in field_names}

        label_texts = {
            'typeofoperations': 'Тип операции',
            'typeofpays': 'Тип оплаты',
            'organizations': 'Организация',
            'bankcards': 'Банковская карта',
            'countrypartyes': 'Контрагент',
        }

        return render(request, 'appay/createform.html',
                      {'field_data': field_data, 'field_names': field_names, 'label_texts': label_texts})

def appay_form(request, pk=None):
    instance = get_object_or_404(ModelPays, pk=pk) if pk else None

    if request.method == 'POST':
        title = request.POST.get('title')
        typeofoperations_name = request.POST.get('typeofoperations_name')
        typeofpays_name = request.POST.get('typeofpays_name')
        organizations_name = request.POST.get('organizations_name')
        bankcards_name = request.POST.get('bankcards_name')
        countrypartyes_name = request.POST.get('countrypartyes_name')
        dateofstart = request.POST.get('dateofstart')
        dateofend = request.POST.get('dateofend')
        comments = request.POST.get('comments')

        typeofoperation_instance = get_object_or_404(typeofoperations, name=typeofoperations_name)
        typeofpay_instance = get_object_or_404(typeofpays, name=typeofpays_name)
        organization_instance = get_object_or_404(organizations, name=organizations_name)
        bankcard_instance = get_object_or_404(bankcards, name=bankcards_name)
        countryparty_instance = get_object_or_404(countrypartyes, name=countrypartyes_name)

        # Получаем объект для обновления
        model_pay = get_object_or_404(ModelPays, id=record_id)

        # Обновляем атрибуты объекта
        model_pay.title = title
        model_pay.typeofoperation = typeofoperation_instance
        model_pay.typeofpay = typeofpay_instance
        model_pay.organization = organization_instance
        model_pay.bankcard = bankcard_instance
        model_pay.countrparty = countryparty_instance
        model_pay.dateofstart = dateofstart
        model_pay.dateofend = dateofend
        model_pay.comments = comments

        # Сохраняем изменения
        model_pay.save()

        return redirect('appay_main')

    field_names = ['typeofoperations', 'typeofpays', 'organizations', 'bankcards', 'countrypartyes', 'deals', 'budgetitems' , 'projects']
    field_data = {field_name: get_items_from_db(field_name) for field_name in field_names}

    label_texts = {
        'typeofoperations': 'Тип операции',
        'typeofpays': 'Тип оплаты',
        'organizations': 'Организация',
        'bankcards': 'Банковская карта',
        'countrypartyes': 'Контрагент',
    }

    return render(request, 'appay/createform.html', {'instance': instance, 'field_data': field_data, 'field_names': field_names, 'label_texts': label_texts})
class ModelPaysAPIView(APIView):
    queryset = ModelPays.objects.all()
    serializer_class = ModelPaysSerializer



# Reg Pay Models
def reg_pay_view(request):
    reg_pay = RegPay.objects.all()
    print(reg_pay)
    return render(request, 'appay/RegPay.html', {'RegPay' : reg_pay})

def reg_pay_createform(request):
    return render(request, 'appay/RegPay_createform.html')