from django.contrib import admin
from .models import Project,Deparment,Employee,Position,ProjectCategory,Sections


class SectionAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")

class ProjectCategoryAdmin(admin.ModelAdmin):
      readonly_fields = ("created","updated")
    
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    list_filter = ("title",)

class PositionAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class DeparmentAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    list_display = ("name","employee_deparments")
    search_fields = ("name",'deparment__name')

    def employee_deparments(self,obj):
        return "".join([obj.deparment.name])

    employee_deparments.short_description = "departamento"


admin.site.register(Sections,SectionAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectCategory,ProjectCategoryAdmin)
admin.site.register(Position,PositionAdmin)
admin.site.register(Deparment,DeparmentAdmin)
admin.site.register(Employee,EmployeeAdmin)