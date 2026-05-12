from django.contrib import admin
from .models import Member
from django.utils.text import slugify


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname','joined_date')
    prepopulated_fields = {"slug":("firstname","lastname")}
    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = slugify(f"{self.firstname} {self.lastname}")

        super().save(*args, **kwargs)
admin.site.register(Member,MemberAdmin)