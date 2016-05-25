"""Views for the mobiles app."""
import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from models import Mobile
from forms import MobileForm

from django.views.generic import View


class MobileView(View):
    """A view for mobiles."""
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request):
        """GET returns a list of objects.

        :param
            request: Httprequest

        :returns
            json response
        """
        if request.GET.get('id'):
            mobiles = Mobile.objects.filter(id=request.GET.get('id')).values()
        else:
            mobiles = Mobile.objects.all()
        return render_to_response('mobiles.json', {'mobiles': mobiles},
            content_type='application/json')

    def post(self, request):
        """POST creates a mobile

        :param
            request : Httprequest

        :returns
            Return a 201 CREATED response or Invalid data
        """
        try:
            data = json.loads(request.body)
        except ValueError:
            return HttpResponseBadRequest('Not valid JSON!')

        form = MobileForm(data)

        if form.is_valid():
            mobile = form.save()
            response = HttpResponse(status=201)
            response['Location'] = '/mobiles/' + str(mobile.id)
            return response
        else:
            return HttpResponseBadRequest('Invalid data!')

    def put(self, request):
        """PUT updates a mobile

        :param
            request : Httprequest

        :returns
            Return a 200 Okay response or Invalid data
        """
        try:
            data = json.loads(request.body)
        except ValueError:
            return HttpResponseBadRequest('Not valid JSON!')

        get_id = Mobile.objects.get(id=data.get('id'))
        form = MobileForm(data, instance=get_id)
        if form.is_valid():
            form.save()
            response = HttpResponse(status=200)
            return response
        else:
            return HttpResponseBadRequest('Invalid data!')

    def delete(self, request):
        """DELETE deletes a mobile

        :param
            request : Httprequest

        :returns
            Return a 200 Okay response or Invalid data
        """
        try:
            data = json.loads(request.body)
        except ValueError:
            return HttpResponseBadRequest('Not valid JSON!')
        Mobile.objects.filter(id=data.get('id')).delete()
        response = HttpResponse(status=200)
        return response
