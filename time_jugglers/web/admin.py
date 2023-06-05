from django.contrib import admin

from time_jugglers.web.models import Profile, Product, Contact, Event


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class ContactAdmin(admin.ModelAdmin):
    pass
