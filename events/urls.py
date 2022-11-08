from django.urls import path, include

urlpatterns = [
    path('api/events/v1/', include('events.api.v1.urls')),
]
