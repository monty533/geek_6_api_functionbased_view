from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'success'})

from datetime import datetime
# do your work here
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'GET'})

    if request.method == 'POST':
        start_time = datetime.now()
        print(request.data)
        if request.data.get('name'):
            uppername = request.data.get('name').upper()
            print(uppername)
        end_time = datetime.now()
        print(f'Duration: {end_time - start_time}')
        return Response({'msg': 'success POST', 'data': request.data})
