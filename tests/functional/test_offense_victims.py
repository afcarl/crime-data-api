# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""
import pytest
from crime_data.common.cdemodels import OffenseVictimCountView
from crime_data.common.base import ExplorerOffenseMapping

class TestVictimsEndpoint:
    def test_state_endpoint_no_year_in_request(self, testapp):
        res = testapp.get('/victims/count/states/3/race_code/offenses')
        assert 'pagination' in res.json
        assert res.status_code == 200
        for r in res.json['results']:
            assert 'count' in r

    @pytest.mark.parametrize('variable', OffenseVictimCountView.VARIABLES)
    def test_victims_offenses_endpoint_with_just_state_year(self, testapp, variable):
        url = '/victims/count/states/43/{}/offenses?year=2014'.format(variable)
        res = testapp.get(url)
        assert 'pagination' in res.json
        for r in res.json['results']:
            assert 'count' in r

    def test_victims_offenses_endpoint_with_state_postal_code(self, testapp):
        url = '/victims/count/states/AR/race_code/offenses?year=2014'
        res = testapp.get(url)
        assert 'pagination' in res.json
        for r in res.json['results']:
            assert 'count' in r

    @pytest.mark.parametrize('variable', OffenseVictimCountView.VARIABLES)
    def test_victims_offenses_endpoint_with_state_year_offense(self, testapp, variable):
        url = '/victims/count/states/43/{}/offenses?offense_name=Aggravated+Assault&year=2014'.format(variable)
        res = testapp.get(url)
        assert 'pagination' in res.json
        for r in res.json['results']:
            assert 'count' in r

    @pytest.mark.parametrize('variable', OffenseVictimCountView.VARIABLES)
    @pytest.mark.parametrize('explorer_offense', ExplorerOffenseMapping.NIBRS_OFFENSE_MAPPING.keys())
    def test_victims_offenses_endpoint_with_state_year_offense(self, testapp, variable, explorer_offense):
        url = '/victims/count/states/43/{}/offenses?explorer_offense={}&year=2014'.format(variable, explorer_offense)
        res = testapp.get(url)
        assert 'pagination' in res.json
        for r in res.json['results']:
            assert 'count' in r