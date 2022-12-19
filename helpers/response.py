from rest_framework.response import Response
from configs.variable_response import *
from math import ceil

def response_data(data=None, status=1, message="Success"):
    result = {
        'status_code': status,
        'message': message,
        'data': data
    }
    return Response(result)

def validate_error(data={}, status=STATUS['INPUT_INVALID']):
    data = dict(data)
    error_message = ''
    for key, value in data.items():
        error_message += str(key) + ' ' + str(list(value)[0])
        break
    return response_data(status=status, message=error_message)

def response_paginator(sum, per_page, data):
    result = {
        'max_page': ceil(sum/per_page),
        'list_data': data
    }
    return response_data(data=result)
