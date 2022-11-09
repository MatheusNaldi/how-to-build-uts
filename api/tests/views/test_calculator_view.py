import json
from unittest import TestCase
from unittest.mock import patch, MagicMock

from rest_framework import status

from api.views.calculator_view import CalculatorView


class CalculatorViewTest(TestCase):
    def setUp(self):
        super().setUp()

        self.calculator_view = CalculatorView()

    def test_get_sum(self):
        with patch(
            "api.views.calculator_view.CalculatorService.sum",
            MagicMock(return_value=8)
        ):
            response = self.calculator_view.get("sum", 6, 2)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            response_body = json.loads(response.content.decode("utf-8"))
            self.assertDictEqual(response_body, {"result": 8})

    def test_get_subtract(self):
        with patch(
            "api.views.calculator_view.CalculatorService.subtract",
            MagicMock(return_value=4)
        ):
            response = self.calculator_view.get("subtract", 6, 2)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            response_body = json.loads(response.content.decode("utf-8"))
            self.assertDictEqual(response_body, {"result": 4})

    def test_get_method_not_found(self):
        with self.assertRaises(Exception) as cm:
            self.calculator_view.get("method_not_found", 2, 3)
            self.assertEqual("Method not found", str(cm.exception))

