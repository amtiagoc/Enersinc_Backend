from django.db import models

# Creating user model here.  
class User(models.Model):
    
    options_tipo_doc = (
        ('CC', 'Cedula de Ciudadania'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cedula de Extranjeria'),
        ('PA', 'Pasaporte'),
    )
    
    options_hobbie = (
        ('1', 'Futbol'),
        ('2', 'Baloncesto'),    
        ('3', 'Tenis'),
        ('4', 'Leer'),
        ('5', 'Cocinar'),
    )
    
    tipo_doc = models.CharField(max_length=10, choices=options_tipo_doc)
    doc = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    hobbie = models.CharField(max_length=10, choices=options_hobbie, default='1')
    objects = models.Manager()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return  self.name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



