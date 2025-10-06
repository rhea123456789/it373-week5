from django.contrib import admin
from pages.models import Post, Comment, Student, Course, Enrollment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "created_at")
    inlines = [CommentInline]
    search_fields = ("title", "body")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author_name", "post", "created_at", "active")
    search_fields = ("author_name", "body")
    list_filter = ("active", "created_at")
    ordering = ("-created_at",)
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "title")
    search_fields = ("code", "title")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "grade")
    search_fields = ("student__first_name", "student__last_name", "course__code", "course__title")
    list_filter = ("course", "grade")



# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("author", "post", "created_at")
#     search_fields = ("author", "text")
#     list_filter = ("created_at",)

# @admin.register(Student)

# @admin.register(Course)

# @admin.register(Enrollment)