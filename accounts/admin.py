from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'website', 'phone') # displays in /admin the filed of the DB

    def user_info(self, obj):
        return obj.description

    # def get_queryset(self, request):
    #     queryset = super(UserProfileAdmin, self).get_queryset(request)
    #     queryset = queryset.order_by('phone', 'user') #primary and secondary ordering / -phone for reverse order
    #     return queryset

    user_info.short_description = 'user_info' #cutomize the column name


admin.site.register(UserProfile, UserProfileAdmin)
