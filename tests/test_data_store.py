import pytest
import json
import os
from unittest.mock import mock_open, patch

from app.data_store import DataHandler

class TestDataHandler():

    @pytest.fixture
    def data_handler_instance(self):
        return DataHandler(json_name="test.json")

    @pytest.fixture
    def json_data(self):
        return {'USD': 1}
    
    def test_creation(self, data_handler_instance):
        data_handler = data_handler_instance

        assert data_handler is not None

    def test_attributes(self, data_handler_instance):
        data_Handler = data_handler_instance

        assert data_Handler.json_path.endswith("data/test.json")
        assert data_Handler.json_path is not None

    def test_read_data(self, data_handler_instance, json_data, mocker):
        
        mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(json_data)))

        data_handler_instance.read_data()

        assert data_handler_instance.data == json_data

    def test_list_stored_currencies(self, data_handler_instance, json_data, mocker):
        mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(json_data)))

        data_handler_instance.read_data()

        assert data_handler_instance.list_stored_currencies() == ["USD"]