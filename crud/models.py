from django.db import models

# Creating user model here.  
class User(models.Model):
    
    tipo_doc = models.CharField(max_length=10)
    doc = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    hobbie = models.CharField(max_length=50)
    objects = models.Manager()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return  self.name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



