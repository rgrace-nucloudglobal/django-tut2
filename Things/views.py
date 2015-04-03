from django.shortcuts import render, get_object_or_404, get_list_or_404
from Things.models import Thing, Shape, Color, TestName
from django.views import generic
from django.conf import settings
from django.core.context_processors import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django import forms
from Things.forms import ThingForm, NameForm
from operator import is_not
from django.contrib.auth.models import User, UserManager
from django.template import RequestContext, loader

# Create your views here.

def index(request):

    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect(reverse('user:login'))
    if user.is_superuser:
        user_things = Thing.objects.order_by('enName')
    else:
        user_things = Thing.objects.filter(user_id=user.id).order_by('enName')
    
    context = {'user_things': user_things, 'user': user, 'show_username': user.is_superuser}
    return render(request, 'Things/index.html', context)

def edit_thing(request, thing_id, user_id):
    
    if request.method == 'POST':
        if 'user_id' in request.POST and (request.POST['user_id'] is None or int(request.POST['user_id']) == 0):
            user = get_object_or_404(User, pk=user_id)
        else:
            user = get_object_or_404(User, pk=request.POST['user_id'])
        
        form = ThingForm()
        
        if thing_id is None or int(thing_id) == 0:
            thing = Thing(user_id=user.id, enName=request.POST['enName'], color_id=request.POST['color_id'], shape_id=request.POST['shape_id'], description=request.POST['description'])
        else:
            thing = Thing(id=request.POST['thing_id'], user_id=user.id, enName=request.POST['enName'], color_id=request.POST['color_id'], shape_id=request.POST['shape_id'], description=request.POST['description'])
        
        thing.save()
#         thing = get_object_or_404(Thing, pk=thing_id)
#         if form.is_valid():
#         - supposed to be able to pull down submitted form values using form.cleaned_data['input_name']
        return HttpResponseRedirect(reverse('Things:index'))

    else:
        if int(thing_id) == 0:
            thing = Thing()
        else:
            thing = get_object_or_404(Thing, pk=thing_id)
        
        form = ThingForm(thing)
        user = request.user
        
    colors = get_list_or_404(Color)
    shapes = get_list_or_404(Shape)
    users = User.objects.all()
    return render(request, 'Things/thing_edit_form.html', {'form': form, 'thing': thing, 'colors': colors, 'shapes': shapes, 'user': user, 'users': users, 'show_username': user.is_superuser})

# def add_name(request):
    
# def delete_thing(request, thing_id):
    
    
def edit_name(request, name_id):
#     testName = TestName(myName=request.method)
    if int(name_id) == 0:
        testName = TestName(myName=None)
    else:
        testName = get_object_or_404(TestName, pk=name_id)
    
    if request.method == 'POST':
        form = NameForm(request.POST)
        
        testName = TestName(id=request.POST['name_id'], myName=request.POST['myName'])
        testName.save()
#         if form.is_valid():
#             testName = TestName(id=form.cleaned_data['name_id'], myName=form.cleaned_data['myName'])
#             testName.save()
    else:
#         testName = get_object_or_404(TestName, pk=name_id)
#         testName = TestName()
        form = NameForm()

    return render(request, 'Things/TestName_form.html', {'form': form, 'testName': testName})

# def detail(request, thing_id):
# return render(request, 'Things:detail.html', {'thing': old_thing,
# 'error_message': 'Failed attempt to persist changes'})


#     if thing_id is None:
#         return render(request, 'Things/detail.html', {'message': 'fshldjfsgh'})
#     else:
#     else:
#         user_thing = Thing.__init__(self)
#     user = request.user
#     user_thing = get_object_or_404(Thing, pk=1)
#
#     colors = get_list_or_404(Color)
#     shapes = get_list_or_404(Shape)
#     context = {'user_thing': user_thing, 'colors': colors, 'shapes': shapes}
# context = {'user_thing': user_thing}
#     return render(request, 'Things/detail.html', context)

def save(request, thing_id):
    #  add exception handling
    SaveException = SaveException
    old_thing = get_object_or_404(Thing, pk=thing_id)
    try:
        old_thing.color_set.get(pk=request.POST['color'])
        old_thing.shape_set.get(pk=request.POST['shape'])
        old_thing.description_set(request.POST['description'])
        old_thing.save()
    except (KeyError, Exception):
        return render(request, 'Things:detail.html', {'thing': old_thing, 'error_message': 'Failed attempt to persist changes'})

    else:
        return HttpResponseRedirect(reverse('Things:detail.html', args=(thing_id)))


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
