from django.contrib import admin
from organization.menu_models import Menu
from organization.models import Club


class BaseClubModelAdmin(admin.ModelAdmin):
    exclude = ('club',)

    def save_model(self, request, obj, form, change):
        club = self.get_club(request)
        if club is not None:
            obj.club = club
        obj.save()

    def get_club(self, request):
        user = request.user
        club = Club.objects.filter(user=user.id)
        if club.exists():
            return club.get()

        return None


class ClubDetailedAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'phone', 'email', 'address', 'work_hours', 'latitude', 'longitude')

    class Media(object):
        css = {'all': ('css/no-more-warnings.css',)}

admin.site.register(Club, ClubDetailedAdmin)
admin.site.register(Menu)