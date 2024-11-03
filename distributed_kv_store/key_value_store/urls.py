from django.urls import path
from .views import StoreDataView, RetrieveDataView

urlpatterns = [
    path('store/', StoreDataView.as_view(), name='store_data'),
    path('retrieve/<str:key>/', RetrieveDataView.as_view(), name='retrieve_data'),
]
