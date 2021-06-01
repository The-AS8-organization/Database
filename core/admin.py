# Importing necessary modules & libraries
from django.contrib import admin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SliderNumericFilter
from core.models import UserAdditionalInfo, Tag, Organization, Initiative, Resource, Consumer



# Changing some features of the admin site
admin.site.site_header = "Database administration"
admin.site.site_title = "Database administration"
admin.site.index_title = "AS8 ORG"



# Creating some admin classes for user-friendly Django model access
class UserAdditionalInfoAdmin(admin.ModelAdmin):
    search_fields = ("user", "github_profile", "discord_username", "social_link")
    list_filter = ("org_task", )

class TagAdmin(admin.ModelAdmin):
    list_display = ("value", )
    search_fields = ("value",)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",  "email", "site", "location", "popularity", "is_active", "is_club")
    search_fields = ("name", "location", "email", "site", "Institution")
    list_filter = ("popularity", "is_club", "is_active", "related_tag")
    filter_horizontal = ("related_tag", )

class InitiativeAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "site", "parent_org")
    search_fields = ("name", "site")
    list_filter = ("date", "parent_org", "related_tag")
    filter_horizontal = ("related_tag", )

class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "link", "parent_org", "can_display")
    search_fields = ("name", "description", "link")
    list_filter = ("date", "can_display", "parent_org", "followed_initiative", "related_tag")
    filter_horizontal = ("followed_initiative", "related_tag")

class ConsumerAdmin(NumericFilterModelAdmin, admin.ModelAdmin):
    list_display = ("name", "email", "age", "location", "profession", "institution", "send_newsletter")
    search_fields = ("name", "email", "location", "profession", "institution", "social_link")
    filter_horizontal = ("initiative_part", )
    list_filter = (("age", SliderNumericFilter), "send_newsletter", "initiative_part")



# Registering Django models.
admin.site.register(UserAdditionalInfo, UserAdditionalInfoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Consumer, ConsumerAdmin)