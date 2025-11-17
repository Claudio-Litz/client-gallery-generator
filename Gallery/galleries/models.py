from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # NOVO CAMPO
    password = models.CharField(
        max_length=128, 
        blank=True, 
        null=True, 
        help_text="Deixe em branco para uma galeria pública."
    )

    def __str__(self):
        return self.title

    # Propriedade para verificar facilmente se é protegida
    @property
    def is_protected(self):
        return bool(self.password)

    # --- NOVO MÉTODO ---
    @property
    def get_cover_image(self):
        """Retorna a URL da primeira foto da galeria, ou None."""
        first_photo = self.photos.first() # Pega a primeira foto
        if first_photo:
            return first_photo.image.url
        return None

class Photo(models.Model):
    # ... (sem mudanças aqui)
    gallery = models.ForeignKey(
        Gallery, 
        on_delete=models.CASCADE, 
        related_name='photos'
    )
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name