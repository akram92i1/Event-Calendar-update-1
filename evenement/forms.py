from django import forms 
from .models import Events_cours,Question_cours,domaine
from django.forms import ModelChoiceField
from django.utils import timezone
from django.http import HttpResponse
from colorama import Fore ,  Back , Style
import colorama
import django.template.loader as Loa
from django.forms.widgets import  Input
from django.forms import widgets  
import datetime 
from django.template import loader 

class Form_Domaine(forms.ModelForm):
    class Meta:
        model = domaine
        fields = [
            'Domain_name',
        ]
#-------------------------------------------------
# for print the value of the question on the select menu 
class UserModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
         return obj.quest
#-------------------------------------------------
class MyAttribute(widgets.FileInput):
    template_name = 'C:/Users/Client Fractal/Desktop/Django_learn/yacine_proj/evenement/templates/bootstrap/Nav_bar/dropfile.html'
    
    def format_value(self, value):
        """
        Return a value as it should appear when rendered in a template.
        """
        if value == '' or value is None:
            return None
        if self.is_localized:
            return formats.localize_input(value)
        return str(value)
    
    def templ_na(self):
        return self.template_name
                             
#-------------------------------------------------
# for print the domain value on the select fields
class UserDomainChoose(ModelChoiceField):
    def label_from_instance(self,obj):
        return obj.Domain_name
#-------------------------------------------------

# ---------------------------------------------------
class Form_question(forms.ModelForm):
        
        Widg =  forms.TextInput(attrs={'size': 10, 'title': 'Your name','required':True ,'class':'form-control col-md-4 shadow p-3' })
        widg2 = forms.Textarea(attrs={'size': 10, 'title': 'Your name','required':False ,'class':'form-control col-md-4 shadow p-3' })

        quest = forms.CharField(widget=Widg)
        rep =  forms.CharField(widget=Widg)
        Fich =forms.FileField(required=False)

        class Meta : 
            model = Question_cours
            fields=['quest' , 'rep' ,'Fich']     


# ---------------------------------------------------     
class Add_cours_Form(forms.ModelForm):
    
    the_quest_value = []
    the_dom_value = []
    list_of_quest = Question_cours.objects.all()
    dom = domaine.objects.all()
    i = 0
    j=0
   
    for target_list in list_of_quest:
        the_quest_value.append(target_list.quest)
        i=i+1
     #------------------------------------------- 
     
     #  for the domain fileds  : 
   
     #--------------------------------------
    for target_list in dom:
        the_dom_value.append(target_list.Domain_name)
        j=j+1
     #---------------------------------------
                
    print("------------- la valeur des champs de Qustion  -----------------------")
    print(the_quest_value)
    print("------------------------------------")
     
    
     
    print("------------- la valeur des champs de domaine  -----------------------")
    print(the_dom_value)
    print("------------------------------------")
     

    i=0
    j=0

    Choice=()
    Choice_Dom = ()
     
    l1 = {}
    l2_for_dom = {}
     
    i=0
    j=0
     
    #---------------------------------------------------
    for k in Question_cours.objects.all():
        l1.update({Question_cours.objects.all()[i]:k.quest})
        i=i+1
      #-------------------------------------------------
    for k in domaine.objects.all():
        l2_for_dom.update({domaine.objects.all()[j]:k.Domain_name}) 
        j=j+1

    l_1_1 = []     
    l2_for_dom_list = []      
     
     
     # the function that return the value  of the fields from a dict 
    def tupl_val(self,val1):
        for i in  self:
            val1.append(i)
            print("the i value is "+str(i))
       
        return val1
     #-----------------------------------------------------
    
     
     
     # to get the name of value of the fields 
    l_1_1 = tupl_val(l1,l_1_1)
    l_1_1=tuple(l_1_1)
    l2_for_dom_list = tupl_val(l2_for_dom,l2_for_dom_list)
    l2_for_dom_list = tuple(l2_for_dom_list)
     #*------------------------------------------
    


     
    
    print("_____________________________")
    print(tuple(the_quest_value))
    print("______________________________")



    print("8=====================>")
    print(l_1_1)
    print("8=====================>")

     
    def make_tuple(self,tup2,index_val):
        res = ()     
        res = (self[index_val],tup2[index_val])
        return res

    hachwa = []
    hachwa_for_domaine = []
    i=0
    j=0
    # this function allows me to return a list of tuple  
    for i in range(0,len(l_1_1)):
        hachwa.append(make_tuple(l_1_1,tuple(the_quest_value),i)) 
     
    for j in range(0,len(l2_for_dom_list)):
        hachwa_for_domaine.append(make_tuple(l2_for_dom_list,tuple(the_dom_value),j))


    print("----><-------")  
    print(Choice)
    print("********")

   

    # creation of a response 
    Widg =  forms.TextInput(attrs={'size': 10, 'title': 'Your name','required':True ,'class':'form-control col-md-4 shadow p-3' })
    widg2 = forms.Select(attrs={'size': 10, 'title': 'Your name','required':True ,'class':'form-control col-md-4 shadow p-3' })
    widg3= forms.NumberInput(attrs={'size': 10, 'title': 'Your name','required':True ,'class':'form-control col-md-4 shadow p-3' })
    widg4 = forms.FileInput(attrs={'size': 10, 'title': 'Your name','required':True ,'class':'form-control shadow p-3  '})
    widg5 = forms.DateTimeInput(attrs={'size': 10, 'title': 'Your name','required':True ,'class':'form-control shadow p-3   ','value':timezone.now()},format='%Y-%m-%d %H:%M')
    widg6 = forms.TextInput(attrs={'size': 10, 'title': 'Your name','required':True ,'class':'form-control col-md-4 shadow p-3' })
    widg8=MyAttribute()
    widg6.format_value(3)
    template = "C:/Users/Client Fractal/Desktop/Django_learn/yacine_proj/evenement/templates/bootstrap/Nav_bar/dropfile.html"
    #widg8 = MyAttribute(widg4)
    s= Loa.get_template(template)  
  

#------------------  The trying zone -------------------------------     
    response = HttpResponse() 
    trst = Input()
    response.write("<div>here is my storm </div>")
    colorama.init()
    print(Fore.YELLOW+"the value is " + str(widg6.get_context(widg4,widg4.format_value(3),attrs={'sizess': 10, 'title': 'Your name','required':True ,'class':'form-control col-md-4 shadow p-3' })))
    print(Fore.YELLOW+"the value of the render function is " + str(widg6.render(widg6,widg6.format_value(3),attrs={'sizess': 10, 'title': 'Your name','required':True ,'class':'form-control col-md-4 shadow p-3' })))
    print(Fore.BLUE+"The value of the seconde function is : "+str(widg6.render(widg6,3)))
    print(Fore.GREEN+"The value of the seconde function is : "+str(type(widg4)))
    print(Style.DIM + 'and in dim text') 
    print(Style.RESET_ALL) 
    print('back to normal now') 
    
#------------------------------------------------------------------
    uploaded_at = forms.CharField(  widget=widg5, required=False)
    domaine =UserDomainChoose(queryset=domaine.objects.all(),label="choose the domain")
    question=UserModelChoiceField(queryset=Question_cours.objects.all(),label="question")
    titre=forms.CharField(widget=Widg, max_length=50,label = "Input the cours Title ")
      
      
    class Meta:
        model = Events_cours
        fields=['titre' , 'domaine' ,'question','uploaded_at']     

     
        
class change(forms.Form):
     model = domaine
     Domain_name = forms.CharField(widget=forms.Textarea)



