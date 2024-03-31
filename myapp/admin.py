from django.contrib import admin

from .models import Hotel, Room, HotelEmployee, Booking, \
    Review, Event, Client, Cancellation, Payment, Service


# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    """Список отелей"""
    list_display = ['name', 'address', 'rating', 'contact_information']
    list_filter = ['rating']
    search_fields = ['name', 'address', 'contact_information']


class RoomAdmin(admin.ModelAdmin):
    """Список номеров"""
    list_display = ['hotel_name', 'type', 'price', 'availability']
    list_filter = ['availability']
    search_fields = ['hotel_name', 'type']

    def hotel_name(self, value):
        return value.hotel_id.name


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['FIO', 'email', 'phone_number', 'country_of_residence']
    search_fields = ['FIO', 'email', 'phone_number', 'country_of_residence']


class BookingAdmin(admin.ModelAdmin):
    """Список бронирований"""
    list_display = ['client_name', 'room_type', 'date_arrival', 'date_departure', 'count_guests', 'status']
    list_filter = ['status']
    search_fields = ['client_name', 'room_type']
    raw_id_fields = ['client_id', 'room_id']

    def client_name(self, value):
        return value.client_id.FIO

    def room_type(self, value):
        return value.room_id.type


class HotelEmployeeAdmin(admin.ModelAdmin):
    """Список сотрудников"""
    list_display = ['hotel_name', 'FIO', 'post', 'contact_information']
    search_fields = ['hotel_name', 'FIO', 'post', 'contact_information']
    raw_id_fields = ['hotel_id']

    def hotel_name(self, value):
        return value.hotel_id.name


class ReviewAdmin(admin.ModelAdmin):
    """Список отзывов"""
    list_display = ['hotel_name', 'client_name', 'amount', 'writing_date']
    search_fields = ['hotel_name', 'client_name']
    raw_id_fields = ['hotel_id', 'client_id']

    def hotel_name(self, value):
        return value.hotel_id.name

    def client_name(self, value):
        return value.client_id.FIO


class EventAdmin(admin.ModelAdmin):
    """Список мероприятий"""
    list_display = ['hotel_name', 'date_and_time', 'name_event', 'description', 'venue']
    search_fields = ['date_and_time', 'name_event', 'hotel_name']
    raw_id_fields = ['hotel_id']

    def hotel_name(self, value):
        return value.hotel_id.name


class CancellationAdmin(admin.ModelAdmin):
    """Список отмен броней"""
    list_display = ['client_FIO', 'date_and_time_references']
    search_fields = ['client_FIO', 'date_and_time_references']
    raw_id_fields = ['booking_id']

    def client_FIO(self, value):
        return value.booking_id.client_id.FIO


class PaymentAdmin(admin.ModelAdmin):
    """Список платежей"""
    list_display = ['client_FIO', 'amount', 'date_and_time']
    search_fields = ['client_FIO', 'amount', 'date_and_time']
    raw_id_fields = ['booking_id']

    def client_FIO(self, value):
        return value.booking_id.client_id.FIO


class ServiceAdmin(admin.ModelAdmin):
    """Список услуг"""
    list_display = ['hotel_name', 'name', 'description', 'price', 'availability']
    search_fields = ['hotel_name', 'price', 'availability']
    raw_id_fields = ['hotel_id']

    def hotel_name(self, value):
        return value.hotel_id.name


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(HotelEmployee, HotelEmployeeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Cancellation, CancellationAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Service, ServiceAdmin)
