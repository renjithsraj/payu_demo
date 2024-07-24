""" The django version is 1.5.1 the imported function mauy varing depands on the versions"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime,hashlib
from django.conf import settings
from util import generate_hash

# Create your views here.

def home(request):
    """ This is the page for requesting the transaction"""
    cleaned_data = {'key': settings.PAYU_INFO['merchant_key'], 
                    'txnid': "asas123", 'amount': 5000, 'productinfo': "sample_produ",
                    'firstname':"renjith", 'email': "re@gmail.com", 'udf1': '', 
                    'udf2': '', 'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '', 'udf7': '', 
                    'udf8': '', 'udf9': '', 'udf10': ''
                    }
    hash_code = generate_hash(cleaned_data)
    return HttpResponse(
         """
            <html>
                    <head><title>Redirecting...</title></head>
                    <body>


                    <form action='%s' method='post' name="payu">

                            <input type="hidden" name="firstname" value="%s" />
                            <input type="hidden" name="surl" value="%s" />
                            <input type="hidden" name="phone" value="%s" />
                            <input type="hidden" name="key" value="%s" />
                            <input type="hidden" name="hash" value =
                            "%s" />
                            <input type="hidden" name="curl" value="%s" />
                            <input type="hidden" name="furl" value="%s" />
                            <input type="hidden" name="txnid" value="%s" />
                            <input type="hidden" name="productinfo" value="%s" />
                            <input type="hidden" name="amount" value="%s" />
                            <input type="hidden" name="email" value="%s" />
                            <input type="hidden" value="submit">
                    </form>
                    </body>
                    <script language='javascript'>


                    window.onload = function(){
                     document.forms['payu'].submit()

                    }

                    </script>
            </html>

                    """ % (settings.PAYU_INFO['payment_url'],
                                 "renjith", 
                                 settings.PAYU_INFO['surl'],
                                 "999990000",
                                 settings.PAYU_INFO['merchant_key'],
                                 hash_code,
                                 settings.PAYU_INFO['curl'],
                                 settings.PAYU_INFO['furl'],
                                 "asas123",
                                 "sample_produ",
                                 "5000",
                                 "xxxxx@gmail.com"
                                 )
        )





def payu_success(request):
    """ we are in the payu success mode"""
    pass
def payu_failure(request):
    """ We are in payu failure mode"""
    pass
def payu_cancel(request):
    """ We are in the Payu cancel mode"""
    pass
