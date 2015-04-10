from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.template import RequestContext, loader

def index(request):
    user = request.user
    if user is None or not user.is_active:
        return HttpResponseRedirect(reverse('user:login'))
    else:
        #         URL_LIST = None
        #         urls = get_urls()
        urls = [{'name': 'User', 'url_name': 'user:index'},
                {'name': 'Things', 'url_name': 'Things:index'}
                ]
        context = {'urls': urls, 'user': user}
        
        return render(request, 'django_tut2_1/index.html', context)
