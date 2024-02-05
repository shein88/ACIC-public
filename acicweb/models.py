from django.db import models
import datetime
import os



# Create your models here.
def getFileName (request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S:")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class VisObjCon(models.Model):
    vision=models.TextField(max_length=1000,null=False,blank=False)
    objectives=models.TextField(max_length=2000,null=False,blank=False)
    contacts=models.TextField(max_length=1000,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"ON: {self.created_at}"

class BoardOfDirectors(models.Model):
    name=models.TextField(max_length=30,null=False,blank=False)
    designation=models.TextField(max_length=30,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"  

class Team(models.Model):
    name=models.TextField(max_length=30,null=False,blank=False)
    designation=models.TextField(max_length=30,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    head=models.BooleanField(default=False,help_text="0-default,1-head")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"      
    
class Collabrations(models.Model):
    government=models.TextField(max_length=1000,null=False,blank=False)
    corporate=models.TextField(max_length=1000,null=False,blank=False)
    academic=models.TextField(max_length=1000,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.created_at}"    

class StartUps(models.Model):
    name=models.TextField(max_length=50,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"     

class Mentors(models.Model):
    name=models.TextField(max_length=50,null=False,blank=False)
    designation=models.TextField(max_length=1000,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    international=models.BooleanField(default=False,help_text="0-default,1-international")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"     
    
class MakersLab(models.Model):
    name=models.TextField(max_length=200,null=False,blank=False)
    description=models.TextField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"
    
class SectorSpecificLab(models.Model):
    name=models.TextField(max_length=200,null=False,blank=False)
    description=models.TextField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}" 

class CommunityInnovativeSpace(models.Model):
    name=models.TextField(max_length=200,null=False,blank=False)
    description=models.TextField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"       

class Events(models.Model):
    name=models.TextField(max_length=100,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"  

class EventNames(models.Model):
    event=models.ForeignKey(Events,on_delete=models.CASCADE)
    name=models.TextField(max_length=500,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.name}"   

class EventDetails(models.Model):
    event=models.ForeignKey(Events,on_delete=models.CASCADE)
    eventname=models.ForeignKey(EventNames,on_delete=models.CASCADE)
    #name=models.TextField(max_length=500,null=False,blank=False)
    venue=models.TextField(max_length=500,null=False,blank=False)
    date=models.DateField(max_length=500,null=False,blank=False)
    image1 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    image2 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    image3 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    image4 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    image5 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    image6 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    image7 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    image8 = models.ImageField(upload_to=getFileName,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name: {self.eventname}"          
    

    