# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""
import pytest
from flex.core import validate_api_call


class TestArrests:
    def test_national_counts(self, testapp, swagger):
        res = testapp.get('/arrests/national')
        assert res.status_code == 200
        validate_api_call(swagger, raw_request=res.request, raw_response=res)
