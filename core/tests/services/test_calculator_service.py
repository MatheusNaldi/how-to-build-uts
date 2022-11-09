from unittest import TestCase

from core.services.calculator_service import CalculatorService

class CalculatorServiceTest(TestCase):
    def setUp(self):
        super().setUp()

        self.calculator_service = CalculatorService()

    def test_sum(self):
        result = self.calculator_service.sum(4, 4)
        self.assertEqual(8, result)

    def test_subtract(self):
        result = self.calculator_service.subtract(5, 4)
        self.assertEqual(1, result)
