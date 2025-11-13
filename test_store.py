from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''


def test_patch_order_by_id():
    order_id = 1
    test_endpoint = f"/store/order/{order_id}"
    patch_data = {
        "status": "shipped",
        "petStatus": "sold"
    }

    response = api_helpers.patch_api_data(test_endpoint, patch_data)

    assert_that(response.status_code, is_(200))
    body = response.json()
    assert_that(body["message"], is_(
        "Order and pet status updated successfully"))
    assert body["orderId"] == order_id
    assert body["status"] == "shipped"
    assert body["petStatus"] == "sold"
