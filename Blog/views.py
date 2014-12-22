from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.middleware.csrf import get_token
from django_common.http import JsonResponse
from Blog.models import TOPIC
from Blog.forms import TOPICForm
def topic_list(request, template='topic/list.html'):
    d = {}
    d['form'] = TOPICForm()
    if request.method == 'POST':
        form = TOPICForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'id': item.id, 'name': str(item), 'form': TOPICForm().as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['topic_list'] = TOPIC.objects.all()
    return render(request, template, d)

from Blog.forms import TOPICForm
def topic_details(request, id, template='topic/details.html'):
    d = {}
    item = get_object_or_404(TOPIC, pk=id)
    d['form'] = TOPICForm(instance=item)
    if request.method == 'POST':
        form = TOPICForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'form': TOPICForm(instance=item).as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['topic'] = TOPIC.objects.get(pk=id)
    return render(request, template, d)

def topic_delete(request, id):
    item = TOPIC.objects.get(pk=id)
    item.delete()
    return JsonResponse()
