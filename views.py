from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from Cyber_Users.models import UserAdd_Model


def admin_login(request):
    if request.method =="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name=='admin' and password == 'admin':
            return redirect('user_details')
    return render(request, 'admins/admin_login.html')


def achart_page(request,chart_type):
    chart = UserAdd_Model.objects.values('year').annotate(dcount=Count('organizationtype'))
    return render(request,'admins/achart_page.html',{'chart_type':chart_type,'objects':chart})

def admin_analysis(request):
    chart = UserAdd_Model.objects.values('attackresult','method').annotate(dcount=Count('attackresult'))
    return render(request,'admins/admin_analysis.html',{'objects':chart})

def user_details(request):
    obj = UserAdd_Model.objects.all()
    return render(request,'admins/user_details.html',{'object':obj})

