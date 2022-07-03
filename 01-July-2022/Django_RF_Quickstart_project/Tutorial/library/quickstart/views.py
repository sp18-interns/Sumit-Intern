from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer


@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'yes its working GET-Method',
            'Method': 'GET',
        })
    elif request.method == 'POST':
        return Response({
            'status': 201,
            'message': 'yes its working POST-Method',
            'Method': 'POST',
        })
    else:
        return Response({
            'status': 404,
            'message': 'yes its working Invalid-Method',
            'Method': 'Null or invalid',
        })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        print(data)
        return Response({
            'status': True,
            'message': 'Good its working',
            'Method': 'Serializer',
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Faulty Response',
        'Method': 'Null or invalid',
    })
    # TodoSerializer
