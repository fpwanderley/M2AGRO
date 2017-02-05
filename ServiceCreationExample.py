from API.models import *
from API.serializers import *


"""
    This dict can be used in a HTTP POST request and this API will create
    a new 'Service' model and its dependencies.
"""

serializer_json = {
    "harvest": 1,
    "name": "Plantio",
    "initial_date": "04/02/2018",
    "final_date": "06/02/2018",
    "service_products": [
        {
            "product": 2,
            "quantity": "500.00",
            "total_cost": "500.00"
        },
        {
            "product": 4,
            "quantity": "200.00",
            "total_cost": "200.00"
        }
    ]
}

serializer = ServiceSerializer(Service(), data=serializer_json)

if serializer.is_valid():
    serializer.save()
else:
    print serializer.errors

