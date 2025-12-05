from django.db import models

class HandmadeItem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(default="No description")
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Handmade Item {self.id}"
