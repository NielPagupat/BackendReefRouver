from django.urls import path
from .views import (
    AcceptRequestHistoryDetailView,
    AllAccessRequestHistoryDetailView,
    DeviceRequestAccessCreateView,
    DeviceRequestAccessDetailView,
    DeviceCreateView,
    DeviceDetailView,
    UserDeviceRequestAccessDetailView,
    AllDeviceRequestAccessListView,
    UserAccessRequestHistoryDetailView
)

urlpatterns = [
    # Device Views
    path('device/create/', DeviceCreateView.as_view(), name='device-create'),  # Create new device
    path('devices/', DeviceDetailView.as_view(), name='device-list'),  # List all devices (ListAPIView)

    # DeviceRequestAccess Views
    path('device-request-access/', DeviceRequestAccessCreateView.as_view(), name='device-request-access-create'),  # Create device access request
    path('device-request-access/<int:pk>/', DeviceRequestAccessDetailView.as_view(), name='device-request-access-detail'),  # View, update, delete access request
    path('user/device-request-access/', UserDeviceRequestAccessDetailView.as_view(), name='user-device-request-access-list'),  # List access requests for authenticated user
    path('device-request-access/all/', AllDeviceRequestAccessListView.as_view(), name='device-request-access-all-list'),  # List all access requests

    # AccessRequestHistory Views
    path('access-request-history/accept/', AcceptRequestHistoryDetailView.as_view(), name='access-request-history-create'),  # Create access request history
    path('access-request-history/', AllAccessRequestHistoryDetailView.as_view(), name='access-request-history-all-list'),  # List all access request history
    path('user/access-request-history/', UserAccessRequestHistoryDetailView.as_view(), name='user-access-request-history-list'),  # List access request history for authenticated user
]
