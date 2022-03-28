from rest_framework import status, views, authentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import pandas as pd
from django.conf import settings



class AccountBalanceView(views.APIView):
    """View for Account Balance"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (AllowAny,)

    def get(self, request):

        default_wallet = settings.ETHEREUM_WALLET

        if default_wallet:
            response = {"message": "Check Account Balance", "default_wallet": f"{default_wallet}"}
        else:
            response = {"message": "Check Account Balance"}

        return Response(response, status=status.HTTP_200_OK)




    def post(self, request):

        wallet_address = request.data["wallet_address"]

        web3 = settings.WEB3
        balance = web3.eth.getBalance(wallet_address)
        # balance_eth = web3.fromWei(balance, 'ether')



        return Response({"account_balance": f"{balance}"}, status=status.HTTP_200_OK)



