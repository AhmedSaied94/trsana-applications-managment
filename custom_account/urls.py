from django.urls import path, include


# app_name = 'custom_account'

urlpatterns = [
    path('auth/', include('allauth.urls'))
]
