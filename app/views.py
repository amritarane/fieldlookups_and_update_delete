from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    QSTO=topic.objects.all()
    QSTO=topic.objects.all().order_by('topic_name')
    QSTO=topic.objects.all().order_by('-topic_name')
    QSTO=topic.objects.filter(topic_name='cricket').order_by('topic_name')
    QSTO=topic.objects.all().order_by(Length('topic_name'))
    QSTO=topic.objects.all().order_by(Length('topic_name').desc())
    QSTO=topic.objects.all()
    QSTO=topic.objects.exclude(topic_name='cricket').order_by('topic_name')
    QSTO=topic.objects.all()[2:4:]
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def insert_topic(request):
    tn=input('enter topic name: ')
    TO=topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    QSTO=topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter()
    QSWO=webpage.objects.filter(Q(topic_name='cricket') & Q(name__startswith='d'))
    QSWO=webpage.objects.filter(Q(topic_name='volleyball') | Q(url__endswith='.in'))
    
    QSWO = webpage.objects.exclude(name__startswith='v')
    QSWO = webpage.objects.exclude(name__endswith='i')
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def insert_webpage(request):
    tn=input('enter topic name: ')
    wn=input('enter name: ')
    ur=input('enter url: ')
    TO=topic.objects.get(topic_name=tn)
    WO=webpage.objects.get_or_create(topic_name=TO,name=wn,url=ur)[0]
    WO.save()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_accessrecords(request):
    QSAO=AccessRecord.objects.all()
    QSAO = AccessRecord.objects.filter(date__year='2023')
    d={'QSAO':QSAO}
    return render(request,'display_accessrecords.html',d)
    
def insert_accessrecords(request):
    wn=input('enter name: ')
    dt=input('enter date: ')
    au=input('enter author: ')
    WO=webpage.objects.get(name=wn)
    AO=AccessRecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
    AO.save()
    QSAO=AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_accessrecords.html',d)

def update_webpage(request):

    webpage.objects.filter(topic_name='cricket').update(url='https//:BCI.cricket.com')
    webpage.objects.filter(name='ram').update(url='https//:ram.in')
    webpage.objects.filter(name='shiv').update(topic_name='basketball')
    webpage.objects.filter(name='kaml').update(topic_name='tenis')
    TO=topic.objects.get(topic_name='hockey')
    webpage.objects.update_or_create(name='vani',defaults={'topic_name':TO})
    webpage.objects.update_or_create(name='sonali',defaults={'topic_name':TO,'url':'https://sonali.in'})
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    
    webpage.objects.filter(Name = 'dhoni').delete()
    
    QSWO = webpage.objects.all()
    d = {'QSWO': QSWO}
    return render(request, 'display_webpage.html', d)