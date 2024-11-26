from django.shortcuts import render
from .serializers import AccessRequestHistorySerializer, DeviceRequestAccessSerializer, DeviceSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import device, DeviceRequestAccess, AccessRequestHistory
# Create your views here.


class DeviceCreateView(CreateAPIView):
    queryset = device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can create devices

class DeviceDetailView(ListAPIView):
    queryset = device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access the device details

class DeviceRequestAccessCreateView(CreateAPIView):
    queryset = DeviceRequestAccess.objects.all()
    serializer_class = DeviceRequestAccessSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can create access requests

class DeviceRequestAccessDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DeviceRequestAccess.objects.all()
    serializer_class = DeviceRequestAccessSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access or modify access requests


class UserDeviceRequestAccessDetailView(ListAPIView):
    serializer_class = DeviceRequestAccessSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access the list

    def get_queryset(self):
        # Filter the queryset by the email of the authenticated user
        user_email = self.request.user.email
        return DeviceRequestAccess.objects.filter(requestee__email=user_email) # Ensure only authenticated users can access or modify access requests

class AllDeviceRequestAccessListView(ListAPIView):
    queryset = DeviceRequestAccess.objects.all()
    serializer_class = DeviceRequestAccessSerializer
    permission_classes = [IsAuthenticated]

class AcceptRequestHistoryDetailView(CreateAPIView):
    queryset = AccessRequestHistory.objects.all()
    serializer_class = AccessRequestHistorySerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access or modify request history

class AllAccessRequestHistoryDetailView(ListAPIView):
    queryset = AccessRequestHistory.objects.all()
    serializer_class = AccessRequestHistorySerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access or modify request history

class UserAccessRequestHistoryDetailView(ListAPIView):
    serializer_class = AccessRequestHistorySerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access the list

    def get_queryset(self):
        # Filter the queryset by the email of the authenticated user
        user_email = self.request.user.email
        # Assuming AccessRequestHistory model is linked to DeviceRequestAccess, filter by requestee's email
        return AccessRequestHistory.objects.filter(accessid__requestee__email=user_email)