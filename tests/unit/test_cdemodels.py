# -*- coding: utf-8 -*-

from crime_data.common.models import RefCounty
from crime_data.common.cdemodels import (CdeRefState,
                                         CdeRefCounty,
                                         CdeRefAgencyCounty,
                                         OffenderCountView,
                                         VictimCountView)
from crime_data.common.marshmallow_schemas import (OFFENDER_COUNT_VARIABLE_ENUM,
                                                   VICTIM_COUNT_VARIABLE_ENUM)
import pytest


class TestCdeRefState:
    def test_get_by_id(self, testapp):
        s = CdeRefState.get(state_id=12).one()
        assert s.state_name == 'Florida'

    def test_get_by_abbr(self, testapp):
        s = CdeRefState.get(abbr='NE').one()
        assert s.state_name == 'Nebraska'

    def test_get_by_fips(self, testapp):
        s = CdeRefState.get(fips='06075').one()
        assert s.state_name == 'California'


class TestCdeRefCounty:
    def test_get_by_id(self, testapp):
        s = CdeRefCounty.get(county_id=753).one()
        assert s.county_name == 'KENDALL'

    def test_get_by_fips(self, testapp):
        s = CdeRefCounty.get(fips='06075').one()
        assert s.county_name == 'SAN FRANCISCO'

        with pytest.raises(ValueError):
            CdeRefCounty.get(fips='6075')

        with pytest.raises(ValueError):
            CdeRefCounty.get(fips=6075)

    def test_get_by_name(self, testapp):
        s = CdeRefCounty.get(name='San Francisco').one()
        assert s.county_name == 'SAN FRANCISCO'

    def test_fips_property(self, testapp):
        state = CdeRefState(state_fips_code='02')
        county = CdeRefCounty(county_fips_code='343', state=state)
        assert county.fips == '02343'

        county = CdeRefCounty(county_fips_code='7', state=state)
        assert county.fips == '02007'

    def test_num_agencies(self, app):
        """Using the test data in the ref_agencies table"""

        county = CdeRefCounty.get(county_id=2271).one()
        assert county.num_agencies_for_year(2014) == 8

    def test_num_agencies_missing_data(self, app):
        """This county is missing current agencies data"""

        county = CdeRefCounty.get(county_id=2271).one()
        assert county.num_agencies is None

    def test_population(self, app):
        """Using the test data in the ref_county_population table"""

        county = CdeRefCounty.get(county_id=74).one()
        assert county.population_for_year(1960) == 24501

    def test_population_missing_data(self, app):
        """This county is missing current population data"""

        county = CdeRefCounty.get(county_id=74).one()
        assert county.population is None

    def test_police_officers(self, app):
        """Using the test data in the database"""

        county = CdeRefCounty.get(county_id=3015).one()
        assert county.police_officers_for_year(1977) == 19

    def test_police_officers_missing_data(self, app):

        county = CdeRefCounty.get(county_id=3015).one()
        assert county.police_officers_for_year(2021) is None
        assert county.police_officers is None


class TestCdeRefAgencyCounty:
    def test_current_year(self, testapp):
        assert CdeRefAgencyCounty.current_year() == 2016


class TestCdeRefState:
    """Test the CdeRefState class"""

    def test_population(self, app):
        state = CdeRefState.get(abbr='WY').one()
        assert state.population_for_year(1984) == 511000

    def test_num_agencies(self, app):
        state = CdeRefState.get(abbr='VA').one()
        assert state.num_agencies == 145

    def test_police_officers(self, app):
        state = CdeRefState.get(abbr='VA').one()
        assert state.police_officers_for_year(2008) == 48


class TestOffenderCountView:
    """Test the OffenderCountView"""

    def test_offender_count_for_a_state(self, app):
        ocv = OffenderCountView(2014, 'race_code', state_id=3)
        results = ocv.query({}).fetchall()

        expected = {'B': 14, 'U': 5, 'W': 4}

        assert len(results) == len(expected)
        for row in results:
            assert row.count == expected[row.race_code]

    @pytest.mark.parametrize('variable', OFFENDER_COUNT_VARIABLE_ENUM)
    def test_offender_count_variables(self, app, variable):
        ocv = OffenderCountView(2014, variable, state_id=3)
        results = ocv.query({}).fetchall()
        assert len(results) > 0


class TestVictimCountView:
    """Test the VictimCountView"""

    def test_victim_count_for_a_state(self, app):
        vcv = VictimCountView(2014, 'offense_name', state_id=3)

        expected = {
            'Aggravated Assault': 12,
            'All Other Larceny': 5,
            'Burglary/Breaking & Entering': 2,
            'Counterfeiting/Forgery': 1,
            'Murder and Nonnegligent Manslaughter': 1,
            'Robbery': 1,
            'Shoplifting': 1,
            'Simple Assault': 5,
            'Theft From Motor Vehicle': 1
        }

        results = vcv.query({}).fetchall()
        assert len(results) == len(expected)
        for row in results:
            assert row.count == expected[row.offense_name]

    @pytest.mark.parametrize('variable', VICTIM_COUNT_VARIABLE_ENUM)
    def test_victim_count_variables(self, app, variable):
        vcv = VictimCountView(2014, variable, state_id=3)
        results = vcv.query({}).fetchall()
        assert len(results) > 0