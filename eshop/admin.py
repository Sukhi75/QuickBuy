from django.contrib import admin

from django.contrib import admin
from .models import Category, Product, PostImage, PostColor, PostSize, ReviewRating

class PostImageAdmin(admin.StackedInline):
    model = PostImage

class PostSizeAdmin(admin.StackedInline):
    model = PostSize

class PostColorAdmin(admin.StackedInline):
    model = PostColor

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin, PostColorAdmin, PostSizeAdmin,]
    list_display = ['name', 'slug', 'price', 'available','weight']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(PostSize)
class PostSizeAdmin(admin.ModelAdmin):
    pass

@admin.register(PostColor)
class PostColorAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    pass
