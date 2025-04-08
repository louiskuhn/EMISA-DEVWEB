from django.db import models
from django.contrib import admin

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur =  models.CharField(max_length=100)
    contenu = models.TextField()

    def __str__(self):
        return self.titre
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "auteur", "contenu")
    list_filter = ("auteur",)