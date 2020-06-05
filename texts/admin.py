from django.contrib import admin

# Register your models here.
from parler.admin import TranslatableAdmin

from .forms import PageTextsAdminForm
from .models import PageTexts


@admin.register(PageTexts)
class PageTextsAdmin(TranslatableAdmin):
    save_on_top = True
    list_display = ('name', )
    form = PageTextsAdminForm

    class Meta:
        proxy = True

    # def has_delete_permission(self, request, obj=None):
    #     # Disable delete
    #     return False
    #
    def has_add_permission(self, request):
        # Disable add
        return False

