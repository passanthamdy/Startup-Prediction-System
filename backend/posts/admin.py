from django.contrib import admin
from .models import Post,Dataset
# Register your models here.

admin.site.register(Dataset)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','title','content','image','featured','created_at']
    fieldsets = (
        (None, {'fields': ( 'title','content','image',  'likes','featured','created_at','slug',)
        }),
    )
    readonly_fields = ['created_at','slug']

    def save_model(self, request, obj, form, change):
        obj.user= request.user
        return super().save_model(request, obj, form, change)
