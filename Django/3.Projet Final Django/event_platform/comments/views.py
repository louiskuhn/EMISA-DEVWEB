from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Comment
from events.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect('event_detail', pk=event_id)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {'form': form, 'event': event})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.event.pk})
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user
