from django.contrib import admin
from django.utils.html import format_html
from .models import (
    PersonalInfo, Skill, Experience, Project, 
    Education, Achievement, Contact, SiteSettings
)

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone', 'location', 'is_active', 'updated_at']
    list_editable = ['is_active']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'description', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order', 'is_active']
    list_editable = ['category', 'proficiency', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    ordering = ['category', 'order', 'name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_current', 'is_active', 'start_date']
    search_fields = ['title', 'company', 'description']
    ordering = ['-start_date', 'order']
    fieldsets = (
        ('Position Details', {
            'fields': ('title', 'company', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Content', {
            'fields': ('description', 'achievements', 'technologies_used')
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'is_active', 'created_at']
    list_editable = ['is_featured', 'order', 'is_active']
    list_filter = ['is_featured', 'is_active', 'technologies']
    search_fields = ['title', 'description']
    ordering = ['order', '-created_at']
    filter_horizontal = ['technologies']
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'short_description', 'image')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Technologies & Display', {
            'fields': ('technologies', 'order', 'is_featured', 'is_active')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'location', 'start_date', 'end_date', 'is_current', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_current', 'is_active', 'start_date']
    search_fields = ['degree', 'institution']
    ordering = ['-start_date', 'order']
    fieldsets = (
        ('Education Details', {
            'fields': ('degree', 'institution', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Additional Information', {
            'fields': ('description', 'gpa')
        }),
        ('Display', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'organization', 'order', 'is_active']
    list_editable = ['year', 'order', 'is_active']
    list_filter = ['year', 'is_active']
    search_fields = ['title', 'organization', 'description']
    ordering = ['-year', 'order']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title', 'is_active', 'updated_at']
    list_editable = ['is_active']
    readonly_fields = ['updated_at']
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

# Customize admin site
admin.site.site_header = "Dipak Kandel Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
