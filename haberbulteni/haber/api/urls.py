from django.urls import path
from haber.api import views as api_views

urlpatterns = [
    path('makaleler', api_views.makale_list_create_api_view, name="makale-listesi"),
]
