from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import Form_Domaine,Form_question,Add_cours_Form,change
from django.contrib.auth import logout
from django.conf import settings 
from .models import Question_cours , Events_cours ,domaine
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
import calendar
import datetime
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from django.urls import reverse
from .utils import EventCalendar
from .HandleCalendaRTag import HandleCalendartag 
from .models import Events_cours
from django.http import Http404

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        render(request , 'bootstrap/page_learn.html')
    else:
        # Return an 'invalid login' error message.
        render(request , 'bootstrap/page_learn.html')

def logout_view(request):
    logout(request)
    render(request , 'bootstrap/page_learn.html')


#----------------- the index view or the welcome page  -------------
def index_page(request): 

     form = Add_cours_Form(request.POST or None  )
     print("THE TYPE OF REQUEST IS  :"+str(request))
     if form.is_valid() :
        form.save() 
        form = Add_cours_Form(  )
     else : 
        print("no the cleaned data is not ok  ::::> "+str(form.errors))
 
     context = {
        'form' : form 
     }
    
     return render(request , 'bootstrap/page_learn.html',context)
#------------------ end of the view to add ------
# ------- --- - -  to add a domain 
def Add_domain(request):
    form = change()
    if request.method =="POST":
        form = change(request.POST)
    if form.is_valid(): 
       print(form.cleaned_data)
       domaine.objects.create(**form.cleaned_data)
    else:
        print(form.errors)   

    context = {
        'form' : form 
    }

    return render(request , 'bootstrap/Add_Domain.html',context)
#-----------------------------------------------------------------------------
def add_question_cours(request):
    print("......*****...> : "+str(settings.MEDIA_URL))
    form = Form_question( request.POST or None  , request.FILES or None)
    
    if form.is_valid() :
       form.save()
       Form_question()
    else : 
        print(form.errors)
  
    context = { 'form' : form }
    
    return render(request , 'bootstrap/add_question.html',context)
#------------------------------------------------------------------------------
def get_nav_bar(request):
    return render(request ,'bootstrap/Nav_bar/nav_bar.html')    
#-----------------------------------------------------------------------------

def Calendar_print( request, context=None):
     # IT'S ALLOWS TO RETURN FROM THE GET REQUEST THE day__gte VARIABLE 
     after_day = request.GET.get('day__gte', None)
     context = context or {}
     if not after_day : 
        d = datetime.date.today() 
     
     else: 
         try:
             print("i am in the try"+str(after_day))
             split_after_day = after_day.split('-')
             d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
         except : 
             d = datetime.date.today()

     previous_month = datetime.date(year=d.year, month=d.month, day=1)
     previous_month = previous_month - datetime.timedelta(days=1)
     
     # Here we calculate the previous month 
     previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                       day=1)
     last_day = calendar.monthrange(d.year, d.month)
     next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])
     # Here we Calculate the next month 
     next_month = next_month + datetime.timedelta(days=1)  # forward a single day
    
     next_month = datetime.date(year=next_month.year, month=next_month.month,
                                   day=1)  # find first day of next month
     
     print("---->>--->> the after day is "+str(after_day))
     cal = EventCalendar()
     cal.cssclass_month_head = "fc-center"
    
     cal.cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    
     cal.cssclasses_weekday_head = [
     "fc-day fc-widget-content",
     "fc-day fc-widget-content",
     "fc-day fc-widget-content",
     "fc-day fc-widget-content ",
     "fc-day fc-widget-content",
     "fc-day fc-widget-content",
     "fc-day fc-widget-content"]

     
     html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
     print("i am here ------------------------------ THE TC TYPE IS : ",type(html_calendar))
     #html_calendar = html_calendar.replace('<table','<table class ="table-striped"')
     #html_calendar = html_calendar.replace('<tr','<tr class ="row"')
     html_calendar = html_calendar.replace('<td ', '<td  height="100%" width="100%" class="fc-day fc-widget-content fc-tue fc-past " ')
     #html_calendar = html_calendar.replace('<th','<th class="fc-day-header fc-widget-header fc-sun"')
     context = { 
         'calendar':mark_safe(html_calendar) ,
         #CONTENT THE LINK TO THE NEXT MONTH
         'next_month' : reverse('Calendar_print') + '?day__gte=' + str(next_month)            ,
         'previous_month' : reverse('Calendar_print' )+'?day__gte=' + str(
            previous_month) 
     }
     #print("THE CONTENT BEFORE DISPLAY PAGE "+html_calendar)
     return render(request , 'bootstrap/Calenda.html',context)
# the information of the the app_label come from the models 

def Events_deatil(request , app_label):
    # get the objects from the databases 
    print("app_label = ",app_label)
    # the context will be displayed on the page
    template = loader.get_template('page_details.html')
    try : 
        obj = Events_cours.objects.get(id=app_label)
        context={
     "object":obj
      }
    except Events_cours.DoesNotExist :
        HTML = "<h1>Error data not found..</h1>"
        raise Http404('Events Does not exist')
    return HttpResponse(template.render(context,request))
    

   