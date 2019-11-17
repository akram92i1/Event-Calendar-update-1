from calendar import HTMLCalendar 
from datetime import datetime as dtime , date , time 
import datetime 
from .models import Events_cours 
from django.http import HttpResponse
# import learn in 03 05 2019 ---> to load some data directly its use
from django.template import loader 
from django.template.loader import render_to_string 
from colorama import Fore , Style  
from django.template import * 
# ----------------------------------------------------------------
# THIS CLASS DECLARATION ALLOWS TO HANDLE THE HTMLCALENDAR METHOD 
# ---------------------------------------------------------------
class EventCalendar(HTMLCalendar):
    def __init__(self,  events = None ):
        super(EventCalendar,self).__init__()
        self.events = events 
   
    def formatday(self , day , weekday , events ): 
        """
        Return a day as a table cell 
        """    
        events_from_day = events.filter(uploaded_at__day = day )
        events_html ="<ul>" 
        
        for event in events_from_day:
            events_html +="<div>" +event.get_absolute_url()+"</div>"+"<br>"
        events_html += "</ul>"

        if day == 0 :
            return '<td class = "noday"> &nbsp;</td>  '    
        else : 
            print("THE POURCENTAGE S CONATIN ",self.cssclasses[weekday])
            return '<td class ="%s" style="height:120px;width:200px;">%d%s</td>'%(self.cssclasses[weekday],day,events_html)    
#----------------------------------------------------------
    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        print("*************************************")
        # The d variable is get it from the loop and i'ts represent the day of the week the same thing for wd week day  
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        print(Fore.BLUE+"the value of s is ",s)
        print(Style.RESET_ALL)
        return "<tr>%s</tr>" % s        
 #------------------------------------------------------
    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        t = loader.get_template('nav_bar.html')
        print(Fore.LIGHTRED_EX,"THE TEMPLATE CONTENT",t)
        print(Style.RESET_ALL)
        #rendered = render_to_string('nav_bar.html')
    
        
        # Give the data to the databases to get all the result by month 
        events = Events_cours.objects.filter(uploaded_at__month=themonth)

        # DECLARATION OF THE TABLE THAT WILL CONTAIN ALL THE DATA 
        v = []
        a = v.append

        # construction of the table  
        print("--------------4545454")
        a('<div class ="container">')
        a('<table>')
        a('\n')
        print("8================================>-----")  
        # USE A METHODE OF HTML CALENDAR TO RETURN  
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        print("8================================>-----") 
        a('\n')
        a(self.formatweekheader())
        i=1 
        a('\n')
        print(self.monthdays2calendar(theyear, themonth))
        print(events)
        # self.monthdays2calendar ==> it's a method thats return the week  
        a('<tbody>')
        for week in self.monthdays2calendar(theyear, themonth):
            print("the week ===> ",week)
            a(self.formatweek(week, events))
            i=i+1
            a('\n')
        a('</tbody>')
        a('</table>')
        a('</div>')
        a('\n')
        return ''+''.join(v)   