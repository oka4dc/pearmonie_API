
from django.db import models

# Create your models here.


class Store(models.Model):
    """Define parameters for creating product catergory

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    Name = models.CharField(max_length=255, null=False)
    Description = models.TextField(blank=True, null=True)
    Address = models.TextField()
    Updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Stores'
    def __str__(self):
        return self.Name

