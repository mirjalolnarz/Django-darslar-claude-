# posts/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Ro'yxatda ko'rinadigan ustunlar
    list_display = ('title', 'published', 'suz_soni', 'created_at')

    def suz_soni(self, obj):
        return len(obj.content.split())
    suz_soni.short_description = 'So\'z Soni'  # Admin panelida ustun nomi

    # O'ng tomondagi filter paneli
    list_filter = ('published', 'created_at')

    # Qidiruv qaysi maydonlar bo'yicha ishlaydi
    search_fields = ('title', 'content')

    # Ro'yxatdan to'g'ridan-to'g'ri tahrirlash
    list_editable = ('published',)

    # URL uchun avtomatik slug
    prepopulated_fields = {'slug': ('title',)}

    # Tahrirlash sahifasida ko'rinadigan maydonlar
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'slug', 'content')
        }),
        ('Sozlamalar', {
            'fields': ('published',),
            'classes': ('collapse',)  # Bu bo'limni yashirish uchun
        }),
    )

    # Ro'yxatda qancha element ko'rsatiladi
    list_per_page = 20

    # Sana bo'yicha navigatsiya
    date_hierarchy = 'created_at'