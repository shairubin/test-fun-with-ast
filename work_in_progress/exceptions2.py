import logging
import sys
from functools import wraps

from asgiref.sync import iscoroutinefunction, sync_to_async

from django.conf import settings
from django.core import signals
from django.core.exceptions import ( # issue #54 in fun-with-ast
    BadRequest,
    PermissionDenied,
    RequestDataTooBig,
    SuspiciousOperation,
    TooManyFieldsSent,
    TooManyFilesSent)
from django.http import Http404
from django.http.multipartparser import MultiPartParserError
from django.urls import get_resolver, get_urlconf
from django.utils.log import log_response
from django.views import debug


def convert_exception_to_response(get_response):

    if iscoroutinefunction(get_response):

        @wraps(get_response)
        async def inner(request):
            try:
                response = await get_response(request)
            except Exception as exc:
                response = await sync_to_async(
                    response_for_exception, thread_sensitive=False
                )(request, exc)
            return response

        return inner
