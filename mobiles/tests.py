"""
Tests for the mobiles app.
"""
from django.test import TestCase
import mock
import simplejson as json
from models import Mobile
from views import MobileView
from forms import MobileForm
from django.test.client import RequestFactory


class TestMobile(TestCase):
    """Tests for the Mobile model."""
    def test_mobile(self):
        """Test the mobile model."""
        mobile = Mobile()
        mobile.make = 'Make'
        mobile.model = 'Model'
        mobile.year = 1999
        mobile.save()


class TestMobileForm(TestCase):
    """Tests for the mobile form."""
    def test_form(self):
        """Test that the form is attached to the right model."""
        self.assertIs(MobileForm._meta.model, Mobile, 'Should be attached to Mobile.')


class TestIndexView(TestCase):
    """Tests for the mobiles.mobiles_view view."""
    @mock.patch('mobiles.views.MobileForm')
    def test_post(self, MockMobileForm):
        """Test a POST request to the mobile_view view."""
        obj = {'make': 'samsung', 'model': 's7', 'year': 2016}
        request = mock.Mock(
            method='POST',
            body=json.dumps(obj)
        )
        mock_form = MockMobileForm.return_value
        mock_mobile = mock_form.save.return_value
        mock_mobile.id = 123

        response = MobileView.as_view()(request)

        self.assertEqual(response.status_code, 201,
                         'Should return 201 CREATED.')
        self.assertEqual(response['Location'], '/mobiles/123',
                         'Should return the location of the new mobile.')
        MockMobileForm.assert_called_with(obj)
        self.assertTrue(mock_form.save.called, 'Should call save.')

    def test_post_invalid_data(self):
        """Test POSTing invalid data."""
        request = mock.Mock(
            method='POST',
            body='{}'
        )
        mobiles_view = MobileView.as_view()
        response = mobiles_view(request)

        self.assertEqual(response.status_code, 400,
                         'Should return a 400 BAD REQUEST.')

    def test_post_bad_json(self):
        """Test POSTing invalid JSON."""
        request = mock.Mock(
            method='POST',
            body='foo'
        )
        mobiles_view = MobileView.as_view()
        response = mobiles_view(request)

        self.assertEqual(response.status_code, 400,
                         'Should return a 400 BAD REQUEST.')

    @mock.patch('mobiles.views.Mobile')
    def test_get(self, MockMobile):
        """Test GET requests to the mobiles_view view."""
        #request = mock.Mock(method='GET')
        objs = [
            {'id': 1, 'make': 'Make1', 'model': 'Model1', 'year': 1},
            {'id': 2, 'make': 'Make2', 'model': 'Model2', 'year': 2},
            {'id': 3, 'make': 'Make3', 'model': 'Model3', 'year': 3},
        ]
        MockMobile.objects.all.return_value = [Mobile(**obj) for obj in objs]
        factory_request = RequestFactory()
        request = factory_request.get('/mobiles')
        response = MobileView.as_view()(request)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200,
                         'Should return a successful response.')
        self.assertEqual(response['Content-Type'], 'application/json',
                         'Should return a JSON response.')
        self.assertSequenceEqual(data, objs, 'Should return the objects.')

    def test_not_supported(self):
        """Test sending an unsupported request method."""
        #request = mock.Mock(method='FOO')
        factory_request = RequestFactory()
        request = factory_request.head('/mobiles')
        mobiles_view = MobileView.as_view()
        response = mobiles_view(request)
        self.assertEqual(response.status_code, 405,
                         'Should return a 405 NOT ALLOWED.')
        self.assertIn('GET', response['Allow'], 'Should allow GET.')
        self.assertIn('POST', response['Allow'], 'Should allow POST.')
        self.assertIn('PUT', response['Allow'], 'Should allow PUT.')
        self.assertIn('DELETE', response['Allow'], 'Should allow DELETE.')

    def test_post(self):
        """Test sending an post request method."""
        factory_request = RequestFactory()
        data = {"make": "Samsung", "model": "s7", "year": 2016}
        json_data = json.dumps(data)
        request_post = factory_request.post('/mobiles',  content_type='application/json', data=json_data)
        mobiles_view = MobileView.as_view()
        post_response = mobiles_view(request_post)
        get_request = factory_request.get('/mobiles')
        mobiles_view = MobileView.as_view()
        get_response = mobiles_view(get_request)
        data['id'] = 1
        self.assertEqual(json.loads(get_response.content), [data])

    def test_delete(self):
        """Test sending an delete request method."""
        mobile = Mobile()
        mobile.make = 'Make'
        mobile.model = 'Model'
        mobile.year = 2016
        mobile.save()
        obj = {'id': 1}
        request = mock.Mock(
            method='DELETE',
            body=json.dumps(obj)
        )
        response = MobileView.as_view()(request)
        self.assertEquals(response.status_code, 200)
