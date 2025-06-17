from django.contrib import admin
from .models import *
from datetime import timedelta
from django.utils import timezone
from django.utils.timezone import now


class DateRangeFilter(admin.SimpleListFilter):
    title = 'Yuborilgan vaqti'
    parameter_name = 'sent_at_range'

    def lookups(self, request, model_admin):
        return [
            ('1', 'So‘nggi 1 kun'),
            ('7', 'So‘nggi 7 kun'),
            ('30', 'So‘nggi 30 kun'),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(sent_at__gte=now() - timedelta(days=int(value)))
        return queryset


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at', 'is_read')
    list_filter = (DateRangeFilter, 'is_read')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'sent_at')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj and not obj.is_read and request.method == 'GET':
            obj.is_read = True
            obj.save(update_fields=['is_read'])
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'location', 'updated_at')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date')
    search_fields = ('institution',)
    list_filter = ('degree',)


admin.site.register(Experience)
admin.site.register(Work)
admin.site.register(BlogArticle)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'telegram')
