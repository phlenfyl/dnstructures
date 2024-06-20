from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class CarouselImage(models.Model):
    # name = models.CharField(max_length = 100, null= True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    class Meta:
        verbose_name = 'Carousel Image'
        verbose_name_plural = 'Carousel Images'

class ComingSoon(models.Model):
    carousel = models.ForeignKey(CarouselImage, on_delete=models.CASCADE, related_name="carouselsoon")
    image = models.ImageField(upload_to= 'commingsoon', default='', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = 'Coming Soon'
        verbose_name_plural = 'Coming Soon'
    
class LeftImage(models.Model):
    carousel = models.ForeignKey(CarouselImage, on_delete=models.CASCADE, related_name="carouselleft")
    image = models.ImageField(upload_to= 'leftimages', default='', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = 'Left Image'
        verbose_name_plural = 'Left Images'
    
class RightImage(models.Model):
    carousel = models.ForeignKey(CarouselImage, on_delete=models.CASCADE, related_name="carouselright")
    image = models.ImageField(upload_to= 'rightimages', default='', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        verbose_name = 'Right Image'
        verbose_name_plural = 'Right Images'

    
    
    
CATEGORY_CHOICE = [
    ('land', 'Land'),
    ('house', 'House'),
]


class Category(models.Model):
    name = models.CharField(max_length = 500, blank=True, null= True)
    slug =  models.SlugField(unique=True, blank= True, null= True)
    categorychoice = models.CharField(choices=CATEGORY_CHOICE, max_length=500, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Categories"




class Subscribe(models.Model):
    monthly = models.DecimalField(max_digits=10, decimal_places=2, blank= True, null= True) 
    quaterly = models.DecimalField(max_digits=10, decimal_places=2, blank= True, null= True) 
    yearly = models.DecimalField(max_digits=10, decimal_places=2, blank= True, null= True) 

    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.monthly is not None:
            return str(self.monthly)
        return ""

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribe'

class Pricing(models.Model):
    premium = models.DecimalField(max_digits=10, decimal_places=2, blank= True, null= True)
    standard = models.DecimalField(max_digits=10, decimal_places=2, blank= True, null= True)
    regular = models.DecimalField(max_digits=10, decimal_places=2, blank= True, null= True)
    premium_plus = models.DecimalField(max_digits=10, decimal_places=2, blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.premium is not None:
            return str(self.premium)
        return ""

    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing'



class Product(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="housecats", blank= True, null= True)
    landcategory= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="landcats", blank= True, null= True)
    name = models.CharField(max_length= 500, blank= True, null= True)
    slug =  models.SlugField(unique=True, blank= True, null= True, max_length=200)
    info = RichTextField(null= True)
    is_featured = models.BooleanField()
    prices = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name ="price", blank= True, null= True)
    subscribe = models.ForeignKey(Subscribe, on_delete=models.CASCADE, related_name ="subscribe")
    display = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created"]
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}/'



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to= 'productImage', default='', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'