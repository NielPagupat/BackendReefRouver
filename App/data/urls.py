from django.urls import path

from .views import DataEntryCreateView, DataEntryDetailView

urlpatterns = [
    path('data-entries/', DataEntryCreateView.as_view(), name='data-entry-create'),
    path('data-entries/<str:owner_email>/', DataEntryDetailView.as_view(), name='data-entry-detail'),
]

