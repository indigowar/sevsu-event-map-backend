from django.urls import path, include

urlpatterns = [
    path('/v1/', include('events.api.v1.urls')),
]
