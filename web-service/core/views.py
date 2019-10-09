from rest_framework import viewsets
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from django.http import FileResponse, HttpResponseNotFound
from core.models import *
from core.utils.decorators import redirect_if_authorize
from core.utils.exceptions import ErrorResponse
    send_email, get_user_or_none, create_user_from_fields, check_email, \
    is_not_fields_include, check_password, get_links
from web_service.settings import BASE_DIR

import json
import os


def get_records(request):
    records = Record.objects.all()
    ret = json.dumps(records)
    return Response(ret)


def add_record(request):
    rec = Record(body=request.body,
                 headers=request.META
                )
    rec.save()
    return Response(status=200)


def clear_records(request):
    Record.objects.all().delete()
    return Response(status=200)


def main(request):
    return FileResponse(open(BASE_DIR+'/frontend/index.html',
                             'rb'))


def static_delivery(request, path=""):
    if os.path.isfile(BASE_DIR+'frontend/dist/' + path):
        response = FileResponse(open(BASE_DIR+'/frontend/' + path, 'rb'))
        if 'css'in path:
            response['Content-Type'] = 'text/css'
        if 'js' in path:
            response['Content-Type'] = 'text/javascript'

    else:
        response = HttpResponseNotFound
    return response
