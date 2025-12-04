from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    Autor = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=150, null= False)
    Texto = models.TextField()
    Data_criacao = models.DateTimeField(default=timezone.now())
    Data_pub = models.DateTimeField(null = True, blank = True)
    posted = models.BooleanField(default= False)

    def post(self):
        self.posted = True
        self.Data_pub = timezone.now()
        self.save
    
    def occult(self):
        self.posted = False
        self.save

    def __str__(self):
        return f"{self.Titulo}\n{self.Autor}"