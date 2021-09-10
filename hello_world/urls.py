from django.urls import path, include

urlpatterns = [
    path('api/messages/', include('messages_api.urls')),
]
