from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from events.models import Event

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def profile(request):
    created_events = Event.objects.filter(creator=request.user)
    participating_events = Event.objects.filter(participants=request.user)
    context = {
        'created_events': created_events,
        'participating_events': participating_events,
    }
    return render(request, 'accounts/profile.html', context)
