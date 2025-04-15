from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event
from .forms import EventForm
from datetime import datetime

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 5
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Récupération du paramètre de recherche par titre
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        # Récupération des dates de début et fin
        date_from_query = self.request.GET.get('date_from', '')
        date_to_query = self.request.GET.get('date_to', '')

        if date_from_query:
            try:
                # Conversion de la chaîne en objet date
                date_from = datetime.strptime(date_from_query, "%Y-%m-%d").date()
                queryset = queryset.filter(date__date__gte=date_from)
            except ValueError:
                pass

        if date_to_query:
            try:
                date_to = datetime.strptime(date_to_query, "%Y-%m-%d").date()
                queryset = queryset.filter(date__date__lte=date_to)
            except ValueError:
                pass

        return queryset

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.creator

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.creator

def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user.is_authenticated:
        event.participants.add(request.user)
    return redirect('event_detail', pk=pk)

def unregister_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.user.is_authenticated:
        event.participants.remove(request.user)
    return redirect('event_detail', pk=pk)
