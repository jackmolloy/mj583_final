from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from nc_biz.finance.models import Company

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
