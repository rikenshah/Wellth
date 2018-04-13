from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'lesson'
urlpatterns = [
    # path('', views.index, name='index'),
    path('profile',login_required(views.profile),name='health_profile'),
	path('handle',login_required(views.handle_profile),name='handle'),
    path('input', login_required(views.HealthProfileCreate.as_view(template_name="health/form.html")), name='health_new'),
    path('update/<pk>', login_required(views.HealthProfileUpdate.as_view(template_name="health/form.html")), name='health_update')
]