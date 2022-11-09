from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

from core.services.calculator_service import CalculatorService

class CalculatorView(APIView):
    def __init__(self):
        self._calculator_service = CalculatorService()

    def get(self, method, number1, number2):
        if method == "sum":
            result = self._calculator_service.sum(number1, number2)
        elif method == "subtract":
            result = self._calculator_service.subtract(number1, number2)
        else:
            raise Exception("Method not found")

        return JsonResponse({"result": result})
