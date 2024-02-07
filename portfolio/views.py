from django.views.generic import ListView
from django.utils import timezone
from .models import UserDetails


class UserHome(ListView):
    model = UserDetails
    template_name = "portfolio/userdetails_list.html"  # Adjust the path based on your project structure
    context_object_name = "User"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ist_time"] = timezone.now().astimezone(timezone.get_current_timezone())
        return context
