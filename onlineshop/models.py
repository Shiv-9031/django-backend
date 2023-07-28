from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    id= models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Category(BaseModel):
    category_name =models.CharField(max_length=100)
    description = models.TextField(max_length=180)

    def __str__(self) -> str:
        return self.category_name


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.FileField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.product_name

class Orders(BaseModel):
    customer_name = models.CharField(max_length=180)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"order # {self.id}"