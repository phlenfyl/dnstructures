from django.contrib import admin
from .models import *

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    
class ComingSoonInline(admin.TabularInline):
    model = ComingSoon
    
class LeftImageInline(admin.TabularInline):
    model = LeftImage
    
class RightImageInline(admin.TabularInline):
    model = RightImage
    

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ("created",)
    inlines = [ComingSoonInline, LeftImageInline, RightImageInline]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ("name","created", "updated")
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    inlines = [ProductImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ("name","created", "updated")
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

admin.site.register([Subscribe, Pricing])