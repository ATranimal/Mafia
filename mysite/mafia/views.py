from django.http import HttpResponse
from django.template import loader

from django.views import generic
from django.core import serializers

from .models import Setup, Role

class IndexView(generic.ListView):
    template_name = 'mafia/index.html'
    context_object_name = 'latest_setup_list'

    def get_queryset(self):
        return Setup.objects.order_by('-name')[:5] 

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context["setups"] = serializers.serialize("json", Setup.objects.all());
        return context

class SetupDetailView(generic.DetailView):
    model = Setup
    template_name = 'mafia/setup_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SetupDetailView, self).get_context_data(**kwargs)

        context["roles"] = serializers.serialize("json", Role.objects.all());
        return context

class RoleDetailView(generic.DetailView):
    model = Role
    template_name = 'mafia/role_detail.html'    

class HowToPlayView(generic.TemplateView):
    template_name = 'mafia/howtoplay.html'   

class RulesetView(generic.TemplateView):
    template_name = 'mafia/ruleset.html'   