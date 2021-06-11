from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User        
class Cour(models.Model):
    
    titre=models.CharField(max_length=200,blank=True,null=True)
    dec=models.CharField(max_length=200,blank=True,null=True)
    dt=models.DateField(auto_now=True)
    slug = models.SlugField(_("slug"),null=True, blank=True)
    img=models.FileField(upload_to='images',blank=True,null=True)
    def __str__(self):
        return  self.titre
       
    def save(self,*args,**kwargs):
       if not self.slug:
       	self.slug=slugify(self.titre)
       super(Cour,self).save(*args,**kwargs)	

class Devoir(models.Model):
    titre=models.CharField(max_length=200,blank=True,null=True)
    dec=models.CharField(max_length=200,blank=True,null=True)
    dt=models.DateField(auto_now=True)
    files=models.FileField(upload_to='Docs')
    def __str__(self):
        return self.titre
    cour=models.ForeignKey(Cour, on_delete=models.CASCADE,default=0) 

class Document(models.Model):
    titre=models.CharField(max_length=200,blank=True,null=True)
    dec=models.CharField(max_length=200,blank=True,null=True)
    dt=models.DateField(auto_now=True)
    files=models.FileField(upload_to='Docs')
    def __str__(self):
        return self.titre
    cour=models.ForeignKey(Cour, on_delete=models.CASCADE,default=0) 
           
class Exam(models.Model):
    titre=models.CharField(max_length=200,blank=True,null=True)
    dec=models.CharField(max_length=200,blank=True,null=True)
    dt=models.DateField(auto_now=True)
    files=models.FileField(upload_to='Docs')
    def __str__(self):
        return self.titre
    cour=models.ForeignKey(Cour, on_delete=models.CASCADE,default=0) 
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    doc=models.ForeignKey(Document,on_delete=models.CASCADE,blank=True)
    content=models.TextField(max_length=1000,blank=False,null=False)
    dat=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
class Annonce(models.Model):
    titre=models.CharField(max_length=30,blank=True,null=True)
    dec=models.TextField(max_length=300)
    dt= models.DateField(auto_now=True)  
    cour=models.ForeignKey(Cour, on_delete=models.CASCADE,default=0)  
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.titre
     