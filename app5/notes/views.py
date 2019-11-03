from django.views.generic import RedirectView, TemplateView, UpdateView

class Notes(TemplateView):
    template_name = 'home.html'
    
