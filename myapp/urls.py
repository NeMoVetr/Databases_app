from django.urls import path

from .views import payment_add, room_add, event_add, hotel_add, client_add, review_add, booking_add, service_add, \
    cancellation_add, hotel_employee_add, cancellation_show, event_show, hotel_show, review_show, rooms_show, \
    clients_show, bookings_show, hotel_employee_show, service_show, payment_show, available_rooms, rooms_in_price_range

urlpatterns = [
    path('payment-add', payment_add, name='payment_add'),
    path('room-add', room_add, name='room_add'),
    path('event-add', event_add, name='event_add'),
    path('hotel-add', hotel_add, name='hotel_add'),
    path('client-add', client_add, name='client_add'),
    path('review-add', review_add, name='review_add'),
    path('booking-add', booking_add, name='booking_add'),
    path('service-add', service_add, name='service_add'),
    path('cancellation-add', cancellation_add, name='cancellation_add'),
    path('hotel-employee-add', hotel_employee_add, name='hotel_employee_add'),
    path('cancellation-show', cancellation_show, name='cancellation_show'),
    path('event-show', event_show, name='event_show'),
    path('hotel-show', hotel_show, name='hotel_show'),
    path('review-show', review_show, name='review_show'),
    path('rooms-show', rooms_show, name='rooms_show'),
    path('clients-show', clients_show, name='clients_show'),
    path('bookings-show', bookings_show, name='bookings_show'),
    path('hotel-employee-show', hotel_employee_show, name='hotel_employee_show'),
    path('service-show', service_show, name='service_show'),
    path('payment-show', payment_show, name='payment_show'),
    path('available-rooms', available_rooms, name='available_rooms'),
    path('rooms-price', rooms_in_price_range, name='rooms_in_price_range'),

]
