import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import status, APIView

def SendResponse(result, data):
	return JsonResponse( { "Result": result, "Data": data })

class ApiDemo(APIView):
	def get(self, *args, **kwargs):
		return SendResponse("Success", {})
