from rest_framework import viewsets
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from django.http import FileResponse, HttpResponseNotFound, HttpResponse
from core.models import *
from core.utils.decorators import redirect_if_authorize
from core.utils.exceptions import ErrorResponse
from web_service.settings import BASE_DIR
import json
import os
from django.core import serializers

def get_records(request):
    records = Record.objects.all()
    ret = serializers.serialize("json", records)
    return HttpResponse(ret)


def add_record(request):
    rec = Record(body=request.body,
                 headers=request.META
                )
    rec.save()
    return HttpResponse(f'\request body: "{request.body}", request META: "{request.META}"')


def clear_records(request):
    Record.objects.all().delete()
    return HttpResponse()   


def main(request):
    return FileResponse(open(BASE_DIR+'/frontend/index.html',
                             'rb'))


def static_delivery(request, path=""):
    p = BASE_DIR + '/frontend/' + path
    print(f'requested path {p}')
    if os.path.isfile(p):
        response = FileResponse(open(p))
        if 'css'in path:
            response['Content-Type'] = 'text/css'
        if 'js' in path:
            response['Content-Type'] = 'text/javascript'

    else:
        response = HttpResponseNotFound
    return response
