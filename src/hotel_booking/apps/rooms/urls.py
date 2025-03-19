from django.urls import path
from .views import RoomCreateView, RoomDeleteView, RoomListView

urlpatterns = [
    path('create/', RoomCreateView.as_view(), name='room-create'),
    path('delete/<int:room_id>/', RoomDeleteView.as_view(), name='room-delete'),
    path('list/', RoomListView.as_view(), name='room-list'),
    path('', RoomListView.as_view(), name='room-root')
]