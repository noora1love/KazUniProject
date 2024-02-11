from django.shortcuts import render

# Create your views here.
def regpay_home(request):
    return render(request, 'regpay/regpay.html')

def regpay_createform(request):
    return render(request, 'regpay/createform.html')

def regpay_form(request):
    return render(request, 'regpay/form.html')