import pytest
import requests
from lambda_forge.constants import BASE_URL

@pytest.mark.integration(method="GET", endpoint="/hello_stamp")
def test_hello_stamp_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/hello_stamp")

    assert response.status_code == 200 
