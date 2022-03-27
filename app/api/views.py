from rest_framework import status, views, authentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import pandas as pd




class AccountBalanceView(views.APIView):
    """View for Account Balance"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({"message": "Check Account Balance"}, status=status.HTTP_200_OK)

    def post(self, request):
        wallet_id = request.data["wallet_id"]

        return Response({"message": f"{wallet_id}"}, status=status.HTTP_200_OK)



