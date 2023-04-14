from django.urls import path

from .views import (
    AlbumCreateView,
    AlbumListView,
    PhotoListView,
    PhotoTagListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
    AlbumUpdateView,
    AlbumDeleteView
)

app_name = 'photo'

urlpatterns = [
    path('', AlbumListView.as_view(), name='albums'),
    path('<slug:slug>', PhotoListView.as_view(), name='photos'),
    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),
    path('create_album/', AlbumCreateView.as_view(), name='create_album'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
    path('<slug>/update_album/', AlbumUpdateView.as_view(), name='update_album'),
    path('<slug>/delete_album/', AlbumDeleteView.as_view(), name='delete_album')
]