from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, views, filters, authentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.permissions import IsAdminOrReadOnly
from core.models import TokenModel
from api.serializers import TokenModelSerializer
import json


class TokenModelViewSet(viewsets.ModelViewSet):
    """Viewset for Token Model"""
    permission_classes = (IsAdminOrReadOnly, IsAuthenticated)
    serializer_class = TokenModelSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ["name","ticker" ]
    search_fields = ("name","ticker")
    ordering_fields = "__all__"
    queryset = TokenModel.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.order_by('name')



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



class TokenSupplyView(views.APIView):
    """View for Token Supply"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (AllowAny,)

    def get(self, request):

        return Response({"message": "Get Token Supply"}, status=status.HTTP_200_OK)


    def post(self, request):

        id = request.data["token"]
        token = TokenModel.objects.get(id=id)

        abi = json.loads(f'{token.abi}')
        address = token.contract

        web3 = settings.WEB3
        contract = web3.eth.contract(address=address, abi=abi)

        symbol = contract.functions.symbol().call()

        if symbol == "USDT":
            total_supply = contract.functions.totalSupply().call()
        else:
            total_supply_wei = contract.functions.totalSupply().call()
            total_supply = web3.fromWei(total_supply_wei, 'ether')


        return Response({"total_supply": f"{total_supply}", "symbol": f"{symbol}"}, status=status.HTTP_200_OK)