#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm

from myrestaurants.models import Restaurant, Dish


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('user', 'date',)


class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('user', 'date', 'restaurant',)
