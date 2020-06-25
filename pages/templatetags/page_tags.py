from django import template
from django.core.exceptions import ObjectDoesNotExist

from design.models import DesignSettings
from pages.models import ProjectCategory, ProfileCategory
from users.models import CustomUser

register = template.Library()


@register.filter(name='proper_paginate')
def proper_paginate(paginator, current_page, neighbors=1):
    if paginator.num_pages > 2*neighbors:
        start_index = max(1, current_page-neighbors)
        end_index = min(paginator.num_pages, current_page + neighbors)
        if end_index < start_index + 2*neighbors:
            end_index = start_index + 2*neighbors
        elif start_index > end_index - 2*neighbors:
            start_index = end_index - 2*neighbors
        if start_index < 1:
            end_index -= start_index
            start_index = 1
        elif end_index > paginator.num_pages:
            start_index -= (end_index-paginator.num_pages)
            end_index = paginator.num_pages
        page_list = [f for f in range(start_index, end_index+1)]
        return page_list[:(2*neighbors + 1)]
    return paginator.page_range


@register.simple_tag(name='project_categories')
def project_categories():
    return ProjectCategory.objects.all()


@register.simple_tag(name='profile_categories')
def profile_categories():
    return ProfileCategory.objects.all()


@register.simple_tag(name='company')
def company():
    try:
        comp = CustomUser.objects.get(username='company')
    except ObjectDoesNotExist:
        password = CustomUser.objects.make_random_password()
        comp = CustomUser.objects.get_or_create(username='company', password=password)
    return comp


@register.simple_tag(name='logo_size')
def logo_size():
    try:
        des = DesignSettings.objects.language('en').filter(name='design', active=True).first()
        if des and des.active:
            size = des.logo_width + 'x' + des.logo_height
        else:
            size = '120x30'
    except ObjectDoesNotExist:
        size = '120x30'
    return size