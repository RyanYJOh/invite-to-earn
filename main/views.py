from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.response import Response
from http.client import HTTPResponse
from .models import Click, Invitation, Service
from .serializers import InvitationSerializer, ClickSerializer

## 초대 코드/링크 등록
@api_view(['POST'])
@permission_classes((AllowAny,))
def postInvitation(request):
    if request.method == 'GET':
        return HTTPResponse(status=200)
    elif request.method == 'POST':
        posted = request.data

        service_id = posted['service']
        
        # print(request.data)
        # print(request.auth)
        # user = request.auth.user 
        user = request.user
        print('REQUEST.USER가 리턴하는 건 : ', user)
        print('REQUEST.AUTH.USER가 리턴하는 건 : ', request.auth.user)
        type = posted['type']
        invitation = posted['invitation']
        desc = posted['desc']

        new_invitation = Invitation.objects.create(
            servce = Service.objects.get(id=service_id),
            user = user,
            type = type,
            invitation = invitation,
            desc = desc,
        )

        new_invitation.save()

        ## 만약 이거 에러나면, created_at가 없기 때문.
        serializer = InvitationSerializer(data=request.data)

        if serializer.is_valid():    
            return Response(serializer.data, status=200)
  

## Service 등록


## 클릭
