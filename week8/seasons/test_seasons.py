from seasons import get_age
import datetime
import pytest


def test_get_age():
	date_format = '%Y-%m-%d'
	date = datetime.date(2024, 6, 25)
	date_year_ago = (date - datetime.timedelta(days=365)).strftime(date_format)
	date_two_years_ago = (date - datetime.timedelta(days=365*2)).strftime(date_format)
	assert get_age(date_year_ago) == 31_536_000
	assert get_age(date_two_years_ago) == 63_072_000
	with pytest.raises(ValueError):
		get_age('2024/06/25')
