"""Views for the cars app."""
from django.utils import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from cars.models import Car
from cars.forms import CarForm

from django.views.generic import View


class CarView(View):
  """A view for cars."""
  http_method_names = ['get', 'post', 'put', 'delete']

  def get(self, request):
    """GET returns a list of objects.

    :param
        request: Httprequest

    :returns
        json response
    """
    if request.GET.get('id'):
        cars = Car.objects.filter(id=request.GET.get('id')).values()
    else:
        cars = Car.objects.all()
    return render_to_response('cars.json', {'cars': cars},
                                  mimetype='application/json')

  def post(self, request):
      """POST creates a car

      :param
        request : Httprequest

      :returns
        Return a 201 CREATED response or Invalid data
      """
      try:
        data = json.loads(request.body)
      except ValueError:
        return HttpResponseBadRequest('Not valid JSON!')

      form = CarForm(data)

      if form.is_valid():
        car = form.save()
        response = HttpResponse(status=201)
        response['Location'] = '/cars/' + str(car.id)
        return response
      else:
        return HttpResponseBadRequest('Invalid data!')

  def put(self, request):
    """PUT updates a car

    :param
        request : Httprequest

    :returns
        Return a 200 Okay response or Invalid data
    """
    try:
        data = json.loads(request.body)
    except ValueError:
        return HttpResponseBadRequest('Not valid JSON!')

    get_id = Car.objects.get(id=data.get('id'))
    form = CarForm(data, instance=get_id)
    if form.is_valid():
        form.save()
        response = HttpResponse(status=200)
        return response
    else:
        return HttpResponseBadRequest('Invalid data!')

  def delete(self, request):
    """DELETE deletes a car

    :param
        request : Httprequest

    :returns
        Return a 200 Okay response or Invalid data
    """
    try:
        data = json.loads(request.body)
    except ValueError:
        return HttpResponseBadRequest('Not valid JSON!')
    Car.objects.filter(id=data.get('id')).delete()
    response = HttpResponse(status=200)
    return response
