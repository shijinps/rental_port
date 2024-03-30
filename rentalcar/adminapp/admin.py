

# Register your models here.
from django.contrib.admin import DateFieldListFilter
from django.contrib import admin
from .models import Booking, Car, location, location2
#-------------for car details-----------#
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'color', 'license_plate', 'status', 'image','Rent_per_day']
    search_fields = ['make', 'model', 'year', 'color', 'license_plate', 'status']
    list_filter = ['status']

admin.site.register(Car, CarAdmin)

# ----------for location pickup and dropoff------#
class adminlocation(admin.ModelAdmin):
    list_display=['pickuplocation']
admin.site.register(location,adminlocation)

class adminlocation2(admin.ModelAdmin):
    list_display=['Dropoflocation']
admin.site.register(location2,adminlocation2)

# ---------for booking--------#
class adminbook(admin.ModelAdmin):
    list_display=['Name','model','Rental_start_date','Rental_end_date','pickuplocation','Dropoflocation','Rental_status']
    list_filter = [('Rental_start_date', DateFieldListFilter), ('Rental_end_date', DateFieldListFilter), 'Rental_status']
    actions = ['approve_bookings','cancel_bookings']

    def approve_bookings(self, request, queryset):
        updated_count = queryset.update(Rental_status='CONFIRMED')
        self.message_user(request, f"{updated_count} booking(s) successfully approved.")
    approve_bookings.short_description = "Approve selected bookings"

    def cancel_bookings(self, request, queryset):
        updated_count = queryset.update(Rental_status='CANCELLED')
        self.message_user(request, f"{updated_count} booking(s) successfully cancelled.")
    cancel_bookings.short_description = "Cancel selected bookings"

admin.site.register(Booking,adminbook)