from django.contrib import admin
from app.models import Games
@admin.register(Games)
class Games_admin(admin.ModelAdmin):
    list_display=['title','description','slug','price','created_time','update_time','publisher','color']