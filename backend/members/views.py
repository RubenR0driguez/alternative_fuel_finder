from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Members
from .serializers import Membersserializer


@api_view(['GET', 'POST'])
def members_list(request):

    if request.method == 'GET':
        members = Members.objects.all()
        serializer = Membersserializer(members, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Membersserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
