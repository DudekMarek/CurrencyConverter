import pytest
from app.currency import Currency

class TestCurrency:
    
    @pytest.fixture
    def currency_instance(self):
        return Currency(name="Currency", dolar_course=1.24)
    
    def test_creation(self, currency_instance):
        obj = currency_instance

        assert obj is not None

    def test_attributes(self, currency_instance):
        obj = currency_instance

        assert obj.name == "Currency"
        assert obj.dolar_course == 1.24

    def test_return_dict(self, currency_instance):
        obj = currency_instance 

        assert currency_instance.return_dict() == {"Currency": 1.24}

    @pytest.mark.parametrize("currency, dollar", [(1, 1.24), (2, 2.48)])
    def test_convert_to_dollar(self, currency_instance, currency, dollar):
        obj = currency_instance

        dolars_converted = obj.convert_to_dollar(currency)

        assert dolars_converted == dollar

    @pytest.mark.parametrize("quantity, currency_dollar_course ,converted_currency", [(1, 2, 0.62), (3.2, 0.87, 4.56)])
    def test_convert_to_another_currency(self, currency_instance, quantity, currency_dollar_course ,converted_currency):
        obj = currency_instance
        converted_currency_instance = Currency(name="ConvertedCurrency", dolar_course=currency_dollar_course)

        assert obj.convert_to_another_currency(another_currency=converted_currency_instance, quantity=quantity) == converted_currency