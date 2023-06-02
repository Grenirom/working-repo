from django.contrib import admin

from group.models import Group, Student, Teacher

admin.site.register(Teacher)


# admin.site.register(Student)
# admin.site.register(Group)


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher', 'count_of_students', 'list_of_students')

    def count_of_students(self, obj):
        # print(obj, '11111111111111111111111111111')
        qt = obj.student.count()
        # print(qt, '********************************')
        return qt

    def list_of_students(self, obj):
        ls = [x for x in obj.student.all()]
        return ls


@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('student_name', 'list_of_groups')

    def student_name(self, obj):
        return obj

    def list_of_groups(self, obj):
        # print(obj.id, obj.name, obj.last_name, obj.contact)
        # print(obj.groups.Group(), '!!!!!!!!!!!!!')
        return [x for x in obj.groups.all()]
