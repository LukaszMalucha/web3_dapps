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
    permission_classes = (IsAdminOrReadOnly,)
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


class SendEthereumView(views.APIView):
    """View for Sending Ethereum"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (AllowAny,)

    def get(self, request):

        return Response({"message": "Send Ethereum"}, status=status.HTTP_200_OK)


    def post(self, request):

        sender_address = request.data["sender_address"]
        private_key = request.data["private_key"]
        receiver_address = request.data["receiver_address"]
        amount = request.data["amount"]
        gas = request.data["gas"]


        # TURN ON GANACHE
        web3 = settings.GANACHE_WEB3




        # Sign transaction


        # Send transaction
        try:

            # Get the nonce
            nonce = web3.eth.getTransactionCount(sender_address)

            # Build transaction
            tx = {
                "nonce": nonce,
                "to": receiver_address,
                "value": web3.toWei(amount, "ether"),
                "gas": int(gas),
                "gasPrice": web3.toWei('50', 'gwei')
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            tx_hash = web3.toHex(tx_hash)
            return Response({"tx_hash": f"{tx_hash}"}, status=status.HTTP_200_OK)

        except Exception as e:
            error = str(e)
            return Response({"error": f"{error}"}, status=status.HTTP_200_OK)



class GreetingsView(views.APIView):
    """View for Greetings"""
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (AllowAny,)

    def get(self, request):

        return Response({"message": "Send Greetings"}, status=status.HTTP_200_OK)

    def post(self, request):

        # TURN ON GANACHE
        web3 = settings.GANACHE_WEB3

        web3.eth.defaultAccount = web3.eth.accounts[0]

        address = web3.toChecksumAddress(web3.eth.accounts[0])

        # Deploy first
        abi = json.loads('[{"inputs":[],"name":"Greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

        contract = web3.eth.contract(address=address, abi=abi)

        greetings = request.data["greetings"]

        tx_hash = contract.functions.setGreeting(greetings).transact()

        web3.eth.waitForTransactionReceipt(tx_hash)



        return Response({"greetings": f"{greetings}"}, status=status.HTTP_200_OK)
