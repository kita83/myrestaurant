#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm

from myrestaurants.models import Restaurant, Dish


class RestaurantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['rows'] = 1
        self.fields['street'].widget.attrs['rows'] = 1
        self.fields['city'].widget.attrs['rows'] = 1
        self.fields['zipCode'].widget.attrs['rows'] = 1
        self.fields['stateOfProvince'].widget.attrs['rows'] = 1
        self.fields['country'].widget.attrs['rows'] = 1
        self.fields['telephone'].widget.attrs['rows'] = 1
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Restaurant
        exclude = ('user', 'date',)


class DishForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['rows'] = 1
        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['description'].widget.attrs['size'] = 10
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Dish
        exclude = ('user', 'date', 'restaurant',)
