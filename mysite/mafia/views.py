from django.http import HttpResponse
from django.template import loader

from django.views import generic

from django.shortcuts import render, get_object_or_404

from .models import Setup, Role

class IndexView(generic.ListView):
    template_name = 'mafia/index.html'
    context_object_name = 'latest_setup_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Setup.objects.order_by('-playerNumber')[:5] 

    # latest_setup_list = Setup.objects.order_by('-playerNumber')[:5] 
    # context = {
    #     'latest_setup_list': latest_setup_list,
    # }
    # return render(request, 'mafia/index.html', context)

class SetupDetailView(generic.DetailView):
    model = Setup
    template_name = 'mafia/setup_detail.html'

    # setup = get_object_or_404(Setup, pk=setup_id)
    # roleList = setup.roles.all()
    # context = {
    #     'setup': setup,
    #     'roleList': roleList
    # }
    # return render(request, 'mafia/setup_detail.html', context)

class RoleDetailView(generic.DetailView):
    model = Role
    template_name = 'mafia/role_detail.html'    
    # role = get_object_or_404(Role, pk=role_id)
    # setups = role.setup.all()
    # return render(request, 'mafia/role_detail.html', {'role': role,'setups': setups})