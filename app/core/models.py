from datetime import datetime

from django.db import models

from core.utils import content_file_name





class TokenModel(models.Model):
    """Model for ETH Token"""
    name = models.TextField(default="Not Specified", unique=True)
    ticker = models.CharField(max_length=254, default="Not Specified", unique=True)
    contract = models.TextField(default="Not Specified")
    abi = models.TextField(default="Not Specified")
    official_site = models.TextField(default="Not Specified")


    class Meta:
        verbose_name_plural = "Ethereum Tokens"

    def __str__(self):
        return str(self.name) + " (" + str(self.ticker) + ")"
