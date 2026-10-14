import pytest

import request_module

import logging

LOGGER = logging.getLogger(__name__)

def test_search_asteroids_with_sucess():
    # Arrange:
    api_key = "JoZ5NozF7n2cw2URO188dqQbxRHpvspnFrAEdggp"
    #Act:
    response = request_module.make_request(api_key)
    #Assertion:
    assert response.status_code == 200  # Validation of status code  
    data = response.json()  
    # Assertion of body response content:  
    assert len(data) > 0  
    #assert data["element_count"] > 0
    LOGGER.info(data)