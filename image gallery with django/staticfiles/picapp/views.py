from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Photo, Album
from .forms import PhotoForm, AlbumForm
from django import forms
from .filters import SnippetFilter


class AlbumListView(ListView):
    model = Album
    template_name = 'picapp/albums.html'
    context_object_name = 'albums'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Album.objects.filter(is_public=False, submitter=self.request.user) | Album.objects.filter(is_public=True)
        else:
            return Album.objects.filter(is_public=True)


class AlbumUserIsAuthorized(UserPassesTestMixin):

    def get_album(self):
        return get_object_or_404(Album, slug=self.kwargs['slug'])

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_album().submitter or self.get_album().is_public == True
        elif self.request.user.is_anonymous:
            return self.get_album().is_public == True
        else:
            raise PermissionDenied


class PhotoListView(AlbumUserIsAuthorized, ListView):

    template_name = 'picapp/photos.html'
    context_object_name = 'photos'

    def get_queryset(self):
        self.album = get_object_or_404(Album, slug=self.kwargs['slug'])
        if self.request.user.is_authenticated:
            return Photo.objects.filter(album=self.album) & (Photo.objects.filter(is_public=False, submitter=self.request.user) | Photo.objects.filter(is_public=True))
        else:
            return Photo.objects.filter(is_public=True) & Photo.objects.filter(album=self.album)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = self.album
        context['filter'] = SnippetFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class PhotoTagListView(ListView):

    template_name = 'picapp/taglist.html'
    context_object_name = 'tags'

    def get_tag(self):
        return self.kwargs.get('tag')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Photo.objects.filter(tags__slug=self.get_tag()) & (Photo.objects.filter(is_public=False, submitter=self.request.user) | Photo.objects.filter(is_public=True))
        else:
            return Photo.objects.filter(is_public=True) & Photo.objects.filter(tags__slug=self.get_tag())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context


class PhotoViewerIsAuthorized(UserPassesTestMixin):

    def get_photo(self):
        return get_object_or_404(Photo, id=self.kwargs['pk'])

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter or self.get_photo().is_public == True
        elif self.request.user.is_anonymous:
            return self.get_photo().is_public == True
        else:
            raise PermissionDenied


class PhotoDetailView(PhotoViewerIsAuthorized, DetailView):

    model = Photo
    template_name = 'picapp/detail.html'
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):

    form_class = PhotoForm
    template_name = 'picapp/create.html'

    def get_success_url(self):
        return reverse_lazy('photo:photos', kwargs={'slug': self.object.album.slug})

    def get_form_kwargs(self):
        kwargs = super(PhotoCreateView, self).get_form_kwargs()
        kwargs['submitter'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)


class AlbumCreateView(LoginRequiredMixin, CreateView):

    form_class = AlbumForm
    template_name = 'picapp/create_album.html'

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('photo:photos', kwargs={'slug': self.object.slug})


class UserIsSubmitter(UserPassesTestMixin):

    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry.... Access denied!')


class UserIsAlbumSubmitter(UserPassesTestMixin):

    def get_album(self):
        return get_object_or_404(Album, slug=self.kwargs['slug'])

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_album().submitter
        else:
            raise PermissionDenied('Sorry.... Access denied!')


class PhotoUpdateView(LoginRequiredMixin, UserIsSubmitter, UpdateView):

    model = Photo
    form_class = PhotoForm
    template_name = 'picapp/update.html'

    def get_success_url(self):
        return reverse_lazy('photo:photos', kwargs={'slug': self.object.album.slug})

    def get_form_kwargs(self):
        kwargs = super(PhotoUpdateView, self).get_form_kwargs()
        kwargs['submitter'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)


class PhotoDeleteView(LoginRequiredMixin, UserIsSubmitter, DeleteView):

    template_name = 'picapp/delete.html'
    model = Photo

    def get_success_url(self):
        return reverse_lazy('photo:photos', kwargs={'slug': self.object.album.slug})


class AlbumUpdateView(LoginRequiredMixin, UserIsAlbumSubmitter, UpdateView):

    model = Album
    form_class = AlbumForm
    template_name = 'picapp/update_album.html'

    def get_success_url(self):
        return reverse_lazy('photo:photos', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)


class AlbumDeleteView(LoginRequiredMixin, UserIsAlbumSubmitter, DeleteView):

    template_name = 'picapp/delete_album.html'
    model = Album
    success_url = reverse_lazy('photo:albums')
