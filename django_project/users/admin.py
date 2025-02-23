from django.contrib import admin, messages

from .models import User, Order



class OrderInline(admin.TabularInline):
    model = Order
    extra = 1


class OrderStackedInline(admin.StackedInline):
    model = Order
    extra = 1

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'name')
    ordering = ('name', 'age')

    readonly_fields = ('created_at', 'updated_at', 'id', 'name')

    inlines = [OrderInline, OrderStackedInline]

    actions = ['increase_age']

    fieldsets = (
        ('Основное', {
            'fields': ('name', 'email', 'age', 'is_active'),
            'description': 'Основные поля пользователя'
        }),
        ('Дополнительно', {
            'fields': ('created_at', 'updated_at', 'id'),
            'description': 'Дополнительные поля пользователя'
        })
    )

    def increase_age(self, request, queryset):
        for user in queryset:
            user.age = user.age + 10
            user.save()
        self.message_user(request, "Возраст выбранных пользователей увеличен на 10.", level=messages.WARNING)



admin.site.register(User, UserAdmin)
admin.site.register(Order)

admin.site.site_header = "Управление сайтом"
admin.site.site_title = "Админка Django"
admin.site.index_title = "Добро пожаловать в панель управления нашего сайта"