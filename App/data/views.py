from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import DataEntry
from .serializers import DataEntrySerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class DataEntryCreateView(CreateAPIView):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer
    permission_classes = [AllowAny]  # Allow all users to access the POST endpoint

    def perform_create(self, serializer):
        # Set the owner to the authenticated user or None for unauthenticated users
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save()

class DataEntryDetailView(ListAPIView):
    serializer_class = DataEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the owner's email from the URL and return all their entries
        owner_email = self.kwargs.get('owner_email')
        return DataEntry.objects.filter(owner__email=owner_email)