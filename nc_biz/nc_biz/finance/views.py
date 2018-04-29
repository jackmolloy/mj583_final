from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from nc_biz.finance.models import Company
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.


def index(request):
    context = {
        'company_count': Company.objects.count(),
    }
    return render(request, "home.html", context)

def single(request):
    # context = {
    #     'company_info': Company
    # }
    return render(request, "single.html", context)

def company(request, pk):
    company = get_object_or_404(Company, id=pk)
    context = {
        #course = Course.objects.order_by('?'[0])
        'company' : company,
    }
    return render(request, "company.html", context)

def companies(request):
    companies = Company.objects.all()
    context = {
        'companies' : companies
    }
    return render(request, "companies.html", context)

def api(request):
    company = request.GET.get('company')

    companies = Company.objects.all()

    # Get json compatible representation of our countries in a list
    data = {
        "companies": [w.to_json() for w in companies],
    }


    return JsonResponse(data)
