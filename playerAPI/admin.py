from django.contrib import admin
from models import Player, WeekPerformance


class WeekPerformanceInline(admin.TabularInline):
    model = WeekPerformance
    max_num = 16
    verbose_name = 'A players performance for a given week'


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'team', 'total_points')
    inlines = [
        WeekPerformanceInline,
    ]


admin.site.register(Player, PlayerAdmin)
