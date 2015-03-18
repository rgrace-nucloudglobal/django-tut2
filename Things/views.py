from django.shortcuts import render, get_object_or_404, get_list_or_404
from Things.models import Thing, Shape, Color
from django.views import generic
from django.conf import settings
from django.core.context_processors import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.template import RequestContext, loader

# Create your views here.

def index(request):
#     user = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
#     colors = get_object_or_404(Color)
# #     if colors.coundt() == 0:
# #         return render(request, 'Things/index.html')
#     
#     user_things = get_object_or_404(Thing).order_by('enName')
# #     shapes = get_object_or_404(Shape).order_by('enName')
    user = request.user
    user_things = Thing.objects.filter(user_id=user.id).order_by('enName')[:5]
    context = {'user_things': user_things, 'user': user}
    return render(request, 'Things/index.html', context)
    

def detail(request, thing_id):
    
#     if thing_id is None:
#         return render(request, 'Things/detail.html', {'message': 'fshldjfsgh'})
#     else:
#     else:
#         user_thing = Thing.__init__(self)
    user = request.user
    user_thing = get_object_or_404(Thing, pk=1)
    
    colors = get_list_or_404(Color)
    shapes = get_list_or_404(Shape)
    context = {'user_thing': user_thing, 'colors': colors, 'shapes': shapes}
#     context = {'user_thing': user_thing}
    return render(request, 'Things/detail.html', context)

def save(request, thing_id):
    #  add exception handling
    SaveException = SaveException
    old_thing = get_object_or_404(Thing, pk=thing_id)
    try:
        selected_color = old_thing.color_set.get(pk=request.POST['color'])
        selected_shape = old_thing.shape_set.get(pk=request.POST['shape'])
        new_description = old_thing.description_set(request.POST['description'])
    except (KeyError, Exception):
        return render(request, 'Things:detail.html', {'thing': old_thing, 'error_message': 'Failed attempt to persist changes'})
    
    else:
        return HttpResponseRedirect(reverse('Things:detail', args=(thing_id)))
     

# class IndexView(generic.ListView):
#     template_name = 'Things/index.html'
#     context_object_name = 'user_things'
#     
#     def get_queryset(self):
#         """List user's things"""
#         user_things = Thing.objects.filter(user_id=1).order_by('enName')[:5]
#         return user_things
    

# class DetailView(generic.DetailView):
#     model = Thing
#     template_name = 'Things/detail.html'

class SaveException(Exception):
    """an attept to persist changes failed"""
    