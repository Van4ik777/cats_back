from django.contrib import admin
from .models import SpyCat, Mission, Target


@admin.register(SpyCat)
class SpyCatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'breed', 'years_of_experience', 'salary')
    search_fields = ('name', 'breed')
    list_filter = ('breed',)
    ordering = ('-years_of_experience',)


class TargetInline(admin.TabularInline):
    model = Target
    extra = 1
    readonly_fields = ('is_completed',)


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('cat__name',)
    inlines = [TargetInline]

    def has_delete_permission(self, request, obj=None):
        if obj and obj.cat is not None:
            return False
        return super().has_delete_permission(request, obj)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'mission', 'is_completed')
    list_filter = ('is_completed', 'country')
    search_fields = ('name', 'notes')

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if obj:
            if obj.is_completed or obj.mission.is_completed:
                readonly.append('notes')
            readonly.extend(['mission', 'is_completed'])
        else:
            readonly.extend(['mission', 'is_completed'])
        return readonly
