from django.contrib import admin

# from .models import User, Order
#
# class OrderInline(admin.TabularInline):
#     model = Order
#     extra = 1  # Количество пустых строк для добавления
#
# class OrderStackInline(admin.StackedInline):
#     model = Order  # Указываем связанную модель
#     extra = 1  # Добавляем одну пустую строку для новых записей
#     # fields = ('title', 'publication_date')  # Отображаемые поля
#     can_delete = True  # Разрешаем удаление записей
#
#
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'age', 'created_at')  # Поля для отображения
#     search_fields = ('name', 'email')  # Поля для поиска
#     list_filter = ('created_at', 'name', 'age')  # Фильтры
#     ordering = ('-created_at',)  # Сортировка по умолчанию
#     readonly_fields = ('created_at',)
#     inlines = [OrderInline, OrderStackInline]
#     actions = ['increase_age']
#
#     def increase_age(self, request, queryset):
#         for user in queryset:
#             user.age += 1
#             user.save()
#         self.message_user(request, "Возраст выбранных пользователей увеличен на 1.")
#
#     increase_age.short_description = "Увеличить возраст на 1"
#
#
# admin.site.register(User, UserAdmin)
# admin.site.register(Order)
#
# admin.site.site_header = "Управление сайтом"
# admin.site.site_title = "Админка Django"
# admin.site.index_title = "Добро пожаловать в панель управления"