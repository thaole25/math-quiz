# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random

# Create your views here.
def index(request):
  num1 = random.randint(0, 100)
  num2 = random.randint(0, 100)
  answer = num1 + num2 
  context = {'num1': num1, 'num2': num2, 'answer': answer}
  return render(request, 'sum/index.html', context)