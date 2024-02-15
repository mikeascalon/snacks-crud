from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'
    context_object_name = 'snacks'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'

class SnackCreateView(CreateView):
    model = Snack
    fields = ['title', 'purchaser', 'description']
    template_name = 'snack_create.html'

class SnackUpdateView(UpdateView):
    model = Snack
    fields = ['title', 'purchaser', 'description']
    template_name = 'snack_update.html'

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snack_delete.html'
    success_url = '/'