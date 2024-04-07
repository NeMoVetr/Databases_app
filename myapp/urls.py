from django.urls import path

from .views import hotel_show, rooms_show, clients_show, bookings_show, hotel_employee_show, review_show, \
    payment_show, service_show, event_show, cancellation_show, hotel_add, room_add, client_add, booking_add, \
    hotel_employee_add, review_add, event_add, cancellation_add, service_add, payment_add, hotel_update, room_update, \
    client_update, booking_update, hotel_employee_update, review_update, event_update, cancellation_update, \
    service_update, \
    payment_update, hotel_delete, room_delete, client_delete, booking_delete, hotel_employee_delete, review_delete, \
    payment_delete, event_delete, cancellation_delete, service_delete, available_rooms, rooms_in_price_range, \
    average_room_price, index

urlpatterns = [
    path('', index, name='index'),
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
    path('average-room-price', average_room_price, name='average_room_price'),

    path('hotel-update/<int:id>/', hotel_update, name='hotel_update'),
    path('room-update/<int:id>/', room_update, name='room_update'),
    path('client-update/<int:id>/', client_update, name='client_update'),
    path('booking-update/<int:id>/', booking_update, name='booking_update'),
    path('hotel-employee-update/<int:id>/', hotel_employee_update, name='hotel_employee_update'),
    path('review-update/<int:id>/', review_update, name='review_update'),
    path('event-update/<int:id>/', event_update, name='event_update'),
    path('cancellation-update/<int:id>/', cancellation_update, name='cancellation_update'),
    path('service-update/<int:id>/', service_update, name='service_update'),
    path('payment-update/<int:id>/', payment_update, name='payment_update'),

    path('hotel-delete/<int:id>/', hotel_delete, name='hotel_delete'),
    path('room-delete/<int:id>/', room_delete, name='room_delete'),
    path('client-delete/<int:id>/', client_delete, name='client_delete'),
    path('booking-delete/<int:id>/', booking_delete, name='booking_delete'),
    path('hotel-employee-delete/<int:id>/', hotel_employee_delete, name='hotel_employee_delete'),
    path('review-delete/<int:id>/', review_delete, name='review_delete'),
    path('event-delete/<int:id>/', event_delete, name='event_delete'),
    path('cancellation-delete/<int:id>/', cancellation_delete, name='cancellation_delete'),
    path('service-delete/<int:id>/', service_delete, name='service_delete'),
    path('payment-delete/<int:id>/', payment_delete, name='payment_delete'),
]
