from django.db import models
from Users.models import CustomUser
from catergory.models import Category
# Create your models here.


class Products(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    Name = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)
    Category = models.ForeignKey(Category, related_name='products_catergory', on_delete=models.CASCADE)
    Price = models.FloatField(null=False)
    Stock = models.FloatField(null=False)
    imageUrl = models.URLField()
    Created_by = models.ForeignKey(CustomUser, related_name='product_owner', on_delete=models.CASCADE)
    Updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)  # Track how many times the product is viewed
    
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return '{} {}'.format(self.Price, self.Name)




