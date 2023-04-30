from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *


def index(request):
    return render(request, 'main/index.html')

def response(request):
    query = request.GET 
    female = request.GET['i1-1']
    name = request.GET['i1-2']
    sec_name = request.GET['i1-3']
    city = request.GET['i1-4']
    email = request.GET['i1-5']
    status = request.GET['i1-5']
    female_r = request.GET['i2-1']
    name_r = request.GET['i2-2']
    secname_r = request.GET['i2-3']
    age_r = request.GET['i2-4']
    prof_r = request.GET['i2-5']
    job_r = request.GET['i2-6']
    vk = request.GET['i2-7']
    tel_r = request.GET['i2-8']
    email_r = query.get('i2-9')
    region_r = request.GET['i2-10']
    city_r = request.GET['i2-11']
    residents_r = request.GET['i2-12']
    gl1 = request.GET['i3-1']
    gl2 = request.GET['i3-2']
    gl3 = request.GET['i3-3']
    gl4 = request.GET['i3-4']
    gl5 = request.GET['i3-5']
    q1 = request.GET['i4-1']
    q2 = request.GET['i4-2']
    q3 = request.GET['i4-3']
    q4 = request.GET['i4-4']
    ph1 = request.GET['ph1']
    ph2 = request.GET['ph2']
    element = Response(order_female = female,
                       order_name = name,
                       order_secname = sec_name,
                       city = city,
                       email = email,
                       status = status,
                       female_r = female_r,
                       name_r = name_r,
                       secname_r = secname_r,
                       age_r = age_r,
                       prof_r = prof_r,
                       job_r = job_r,
                       vk = vk,
                       tel_r = tel_r,
                       email_r = email_r,
                       region_r = region_r,
                       city_r = city_r,
                       residents_r = residents_r,
                       gl1 = gl1,
                       gl2 = gl2,
                       gl3 = gl3,
                       gl4 = gl4,
                       gl5 = gl5,
                       q1 = q1,
                       q2 = q2,
                       q3 = q3,
                       q4 = q4,
                       ph1 = ph1,
                       ph2 = ph2)
    element.save()
    return render(request, 'main/response.html')