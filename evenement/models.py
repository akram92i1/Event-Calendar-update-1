from django.db import models
from django.utils import timezone
from django import forms
from django.urls import reverse
import datetime




#==============================================================
class Question_cours(models.Model): 

	quest = models.CharField(max_length = 20 )
	rep = models.CharField(max_length = 20 ,null = True,blank=True)
	Fich = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True , blank = True)
	#==============================================
	def getter(self):
		return self.quest
	#==============================================	
    
#==============================================================

class domaine (models.Model):
    Domain_name = models.CharField(max_length=40, blank=True)


class Events_cours(models.Model): 
    domaine = models.ForeignKey('domaine' , on_delete = models.CASCADE)
    question = models.ForeignKey('Question_cours' , on_delete = models.CASCADE)
    titre = models.CharField(max_length=40, null=True)
    uploaded_at = models.DateTimeField( default = timezone.now(),blank=True, null=True)
    
    class Meta:
        
        abstract = False
    
    
    # return the url that allows me to see the events we have to change it to a another view 
    # Now we gonna change it with an url that will be store in the template 
    def get_absolute_url(self):
        #url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        url = reverse('detail',kwargs={'app_label': self.id})
        return u'<a href="%s" class="fc-day-grid-event fc-event fc-start fc-end  fc-draggable fc-resizable">%s</a>' % (url, "N°::"+str(self.id)+"___title::"+str(self.id))    

    def get_url(self):
        url = u'<a href=href="%s" class="fc-day-grid-event fc-event fc-start fc-end  fc-draggable fc-resizable">'+self.id,self.titre+'</a>'