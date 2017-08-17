from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from myrestaurants.forms import DishForm, RestaurantForm
from myrestaurants.models import Restaurant, RestaurantReview, Dish


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'myrestaurants/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context


class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm
    success_url = reverse_lazy("myrestaurants:restaurant_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)


class DishCreate(CreateView):
    model = Dish
    template_name = 'myrestaurants/form.html'
    form_class = DishForm
    success_url = reverse_lazy("myrestaurants:restaurant_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_valid(form)


class RestaurantUpdate(UpdateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm
    success_url = reverse_lazy("myrestaurants:restaurant_list")


class DishUpdate(UpdateView):
    model = Dish
    template_name = 'myrestaurants/form.html'
    form_class = DishForm
    success_url = reverse_lazy("myrestaurants:restaurant_list")


def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))
