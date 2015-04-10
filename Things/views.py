from django.shortcuts import render, get_object_or_404, get_list_or_404
from Things.models import Thing, Shape, Color, TestName
from django.views import generic
from django.conf import settings
from django.core.context_processors import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django import forms
from Things.forms import ThingForm, NameForm, ThingColorForm, ThingShapeForm
from operator import is_not
from django.contrib.auth.models import User, UserManager
from django.template import RequestContext, loader

def index(request):

    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect(reverse('user:login'))
    if user.is_superuser:
        user_things = Thing.objects.order_by('enName')
    else:
        user_things = Thing.objects.filter(user_id=user.id).order_by('enName')

    context = {'user_things': user_things, 'user': user,
               'show_username': user.is_superuser}
    return render(request, 'Things/index.html', context)

def edit_thing(request, thing_id, user_id):

    if request.method == 'POST':
        if 'user_id' in request.POST and (request.POST['user_id'] is None or int(request.POST['user_id']) == 0):
            user = get_object_or_404(User, pk=user_id)
        else:
            user = get_object_or_404(User, pk=request.POST['user_id'])

        form = ThingForm()

        if thing_id is None or int(thing_id) == 0:
            thing = Thing(user_id=user.id, enName=request.POST['enName'], color_id=request.POST[
                          'color_id'], shape_id=request.POST['shape_id'], description=request.POST['description'])
        else:
            thing = Thing(id=request.POST['thing_id'], user_id=user.id, enName=request.POST['enName'], color_id=request.POST[
                          'color_id'], shape_id=request.POST['shape_id'], description=request.POST['description'])

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

def colors_list(request):

    user = request.user
    if request.method == 'POST':
        # handle post requests here
        pass
    else:
        # handle non-post requests here
        colors = get_list_or_404(Color)

    context = {'colors': colors, 'user': user}
    return render(request, 'Things/colors_index.html', context)

def edit_color(request, user_id, color_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        # handle post requests here

        form = ThingColorForm()

        if color_id is None or int(color_id) == 0:
            color = Color(
                enName=request.POST['enName'], description=request.POST['description'])
        else:
            color = Color(id=request.POST['color_id'], enName=request.POST[
                          'enName'], description=request.POST['description'])

        color.save()

        return HttpResponseRedirect(reverse('Things:colors'))

    else:
        # handle non-post requests here
        if int(color_id) == 0:
            color = Color()
        else:
            color = get_object_or_404(Color, pk=color_id)

        form = ThingColorForm(color)
        user = request.user

    context = {'form': form, 'color': color, 'user': user}
    return render(request, 'Things/thing_color_edit_form.html', context)


def shapes_list(request):

    user = request.user

    shapes = get_list_or_404(Shape)

    context = {'shapes': shapes, 'user': user}
    return render(request, 'Things/shapes_index.html', context)

def edit_shape(request, user_id, shape_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        # handle post requests here

        form = ThingShapeForm()

        if shape_id is None or int(shape_id) == 0:
            shape = Shape(
                enName=request.POST['enName'], description=request.POST['description'])
        else:
            shape = Shape(id=request.POST['shape_id'], enName=request.POST[
                          'enName'], description=request.POST['description'])

        shape.save()

        return HttpResponseRedirect(reverse('Things:shapes'))

    else:
        # handle non-post requests here
        if int(shape_id) == 0:
            shape = Color()
        else:
            shape = get_object_or_404(Shape, pk=shape_id)

        form = ThingColorForm(shape)
        user = request.user

    context = {'form': form, 'shape': shape, 'user': user}
    return render(request, 'Things/thing_shape_edit_form.html', context)
