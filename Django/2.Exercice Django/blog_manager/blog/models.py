from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

class Article(models.Model):
    titre = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    auteur = models.CharField()
    contenu = models.TextField(validators=[MinLengthValidator(10)])
    date_creation = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Pour des URLs lisibles

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        # Générer automatiquement le slug à partir du titre
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

