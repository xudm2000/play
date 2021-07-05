# -*- coding: utf-8 -*-
from django.shortcuts import render

from playStyle.settings import BASE_DIR


def home(request):
    """
    主页
    """
    return render(request, BASE_DIR + '/playStyle/templates/home.html')


def styles(request):
    """
    风格
    """
    return render(request, BASE_DIR + '/playStyle/templates/styles.html', {'week': 1})


def stylesReload(request):
    """
    风格/重新加载图片
    """
    week = request.GET.get('week')
    return render(request, BASE_DIR + '/playStyle/templates/styles.html', {'week': week})


def platform(request):
    """
    平台
    """
    return render(request, BASE_DIR + '/playStyle/templates/platform.html')


def contact(request):
    """
    联系我们
    """
    return render(request, BASE_DIR + '/playStyle/templates/contact.html')
