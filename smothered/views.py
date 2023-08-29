from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')
