from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.response import Response
from http.client import HTTPResponse
from .models import Click, Invitation, Service
from .serializers import InvitationSerializer, ClickSerializer, ServiceSerializer

## 초대 코드/링크 등록
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def postInvitation(request):
    if request.method == 'GET':
        return HTTPResponse(status=200)
    elif request.method == 'POST':
        posted = request.data

        service_id = posted['service']
        user = posted['user_kakao_id']
        type = posted['type']
        invitation = posted['invitation']
        desc = posted['desc']
        
        new_invitation = Invitation.objects.create(
            service = Service.objects.get(id=service_id),
            user_kakao_id = user,
            type = type,
            invitation = invitation,
            desc = desc,
            totalClicks = 0
        )

        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():    
            return Response(serializer.data, status=200)
        else:
            # print('error : ', serializer.errors)
            return JsonResponse({'message' : 'serializer is not valid'})

## Service 등록
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def postService(request):
    if request.method == 'GET':
        return HTTPResponse(status=200)
    elif request.method == 'POST':
        posted = request.data

        new_service = Service.objects.create(
            service_kr = posted['service_kr'],
            service_en = posted['service_en']
        )

        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():    
            return Response(serializer.data, status=200)
        else:
            print('error : ', serializer.errors)
            print('data : ', serializer.initial_data)
            return JsonResponse({'message' : 'serializer is not valid'})


## 클릭
@api_view(['POST'])
@permission_classes((AllowAny,))
def postClick(request):
    if request.method == 'GET':
        return HTTPResponse(status=200)
    elif request.method == 'POST':
        posted = request.data

        ## ip 얻기
        ip = request.META.get('HTTP_X_FORWARDED_FOR')

        if ip:
            this_ip = ip.split(',')[0]
        else:
            this_ip = request.META.get('REMOTE_ADDR')

        this_invitation = Invitation.objects.get(id=posted['invitation'])
        ## 오브젝트 생성
        new_service = Click.objects.create(
            ip_address = this_ip,
            invitation = this_invitation
        )

        ## 해당 invitation의 totalClicks에 +1
        this_invitation.totalClicks += 1
        this_invitation.save()

        serializer = ClickSerializer(data=request.data)
        if serializer.is_valid():    
            return Response(serializer.data, status=200)
        else:
            print('error : ', serializer.errors)
            print('data : ', serializer.initial_data)
            return JsonResponse({'message' : 'serializer is not valid'})

## 검색한 서비스의 invitations
@api_view(['GET'])
@permission_classes((AllowAny,))
def getRandomInvitation(request, service_id):
    this_service = Service.objects.get(pk=service_id)
    this_serv_invi = Invitation.objects.filter(service=this_service).order_by('?')[0]
    
    serializer = InvitationSerializer(this_serv_invi)

    return JsonResponse(serializer.data, status=200)
