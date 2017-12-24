from django.contrib import admin

from .models import Role, Setup, SetupRole

class RolesInLine(admin.TabularInline):
    model = SetupRole
    extra = 3

class SetupAdmin(admin.ModelAdmin):
    # filter_horizontal = ('types",)
    inlines = (RolesInLine, )

admin.site.register(Role)
admin.site.register(Setup, SetupAdmin)
