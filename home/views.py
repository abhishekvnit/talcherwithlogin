from django.shortcuts import render

# Create your views here.
from home.models import TalcherDirect, Engdjango

from django.db.models import Q

from datetime import date, timedelta

import pandas as pd

from django.contrib.auth import authenticate,logout,login
 
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def welcome(request):

    if request.method=="POST":
            
        username= request.POST.get('username')
        password= request.POST.get('password')
        print("auth rec")
        print(username)
        print(password)
        user = authenticate(username= username, password=password)
        print(user)

        if user is not None:
            login(request,user)
            request.session['username'] = username
            # A backend authenticated the credentials
            return render(request, 'welcome.html',{"username" : username})
        else:
            # No backend authenticated the credentials
            return render(request,'index.html')

def schedule(request):

    if request.session.has_key('username'):

        talcherdb= TalcherDirect.objects.all()
        return render(request, 'index.html', {'talcherdb':talcherdb})
    else:
      return render(request, 'login.html', {})

def milestone(request):

    if request.session.has_key('username'):
   
        talcherdb= TalcherDirect.objects.filter(activity='MIL')
        
        return render(request, 'milestone.html', {'talcherdb':talcherdb})
    else:
        return render(request, 'login.html', {})

def civil(request):

    if request.session.has_key('username'):
   
        talcherdb= TalcherDirect.objects.filter(activity='CIV')
        
        return render(request, 'civil.html', {'talcherdb':talcherdb})
    else:
        return render(request, 'login.html', {})

def erection(request):
   

    talcherdb= TalcherDirect.objects.filter(Q(activity='ERC') | Q(activity ='COM'))
    
    return render(request, 'civil.html', {'talcherdb':talcherdb})


def ordering(request):
   

    talcherdb= TalcherDirect.objects.filter(Q(activity='ORD') | Q(activity ='ENQ'))
    
    return render(request, 'civil.html', {'talcherdb':talcherdb})


def sixmonth(request):
   

    startdate= date.today()
    enddate= startdate+ timedelta(days=240)

    

    talcherdb= TalcherDirect.objects.filter(finish__range= [startdate,enddate])

    
    
    return render(request, 'civil.html', {'talcherdb':talcherdb})




def handlelogout(request):
    
    logout(request)
    
    
    return render(request,'index.html')

def engineering(request):
    

    engdb= Engdjango.objects.all().values()
    df= pd.DataFrame(engdb)
    df['sch_date'] = pd.to_datetime(df['sch_date'], format='%Y-%m-%d')
    df['sch_date']= df['sch_date'].dt.to_period('M')
    df['sch_date']=df['sch_date'][0:-4]
    print(df['sch_date'])
    table=pd.pivot_table(df,values='orgn_drg_no', index=['mu'], columns=['sch_date'], aggfunc='count', fill_value=0)
    mydict={
        "df":table.to_html()
    }

   
    return render(request,'engineering.html', context=mydict)