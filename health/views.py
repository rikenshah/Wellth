from django.shortcuts import render
from .models import HealthProfile
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class HealthProfileDisplay(ListView):
    model = HealthProfile

class HealthProfileCreate(CreateView):
    model = HealthProfile
    fields = ['age','height','weight','ailments','tobacco','smoke','drink','exercise','travel_time', 'sleep_time','job_type']
    success_url = reverse_lazy('health:health_profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HealthProfileUpdate(UpdateView):
    model = HealthProfile
    fields = ['age','height','weight','ailments','tobacco','smoke','drink','exercise','travel_time', 'sleep_time','job_type']
    success_url = reverse_lazy('health:health_profile')
