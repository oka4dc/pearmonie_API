from django.db import models

# Create your models here.


class Category(models.Model):
    """Define parameters for creating product catergory

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    title = models.CharField(max_length=255, null=False)
    Description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

