from unittest.case import TestCase

from django.http.request import HttpRequest

from germanium.tools import assert_true, assert_false, assert_equal, assert_is_none

from pyston.utils import rfs

from app.resource import UserResource


class ResourceTestCase(TestCase):

    def test_get_dict_data(self):
        request = HttpRequest()
        request.data = {'Foo': 'bar', 'Baz': [{'Biz': 'buz'}, {'Biz': 'bez'}], 'Brr': {'Baa': 'bee'}}
        resource = UserResource(request)
        resource.DATA_KEY_MAPPING = {
            'foo': 'Foo',
            'baz': ('Baz', {'biz': 'Biz'}),
            'brr': ('Brr', {'baa': 'Baa'}),
        }
        assert_equal(
            resource.get_dict_data(),
            {'baz': [{'biz': 'buz'}, {'biz': 'bez'}], 'brr': {'baa': 'bee'}, 'foo': 'bar'}
        )
