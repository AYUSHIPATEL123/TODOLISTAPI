from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def index(request):
    data = {
        "name": "to-do API",
        "version": "1.0.0"
    }
    return Response(data)