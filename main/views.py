from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.response import Response
from http.client import HTTPResponse
from .models import Click, Invitation, Service
from .serializers import InvitationSerializer, ClickSerializer, ServiceSerializer
from django.db.models import Q

## 초대 코드/링크 등록
@api_view(['POST'])
@permission_classes((AllowAny,))
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

        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():        
            Invitation.objects.create(
                service = Service.objects.get(id=service_id),
                user_kakao_id = user,
                type = type,
                invitation = invitation,
                desc = desc,
                totalClicks = 0
            )
            return Response(serializer.data, status=200)
        else:
            # print('error : ', serializer.errors)
            return JsonResponse({'message' : 'serializer is not valid'})

## Service 등록
@api_view(['POST'])
@permission_classes((AllowAny,))
def postService(request):
    if request.method == 'GET':
        return HTTPResponse(status=200)
    elif request.method == 'POST':
        posted = request.data

        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():    
            Service.objects.create(
                service_kr = posted['service_kr'],
                service_en = posted['service_en']
            )

            ## 해당 서비스의 id 리턴
            this_service_id = Service.objects.get(service_kr=posted['service_kr'], verified=False).id
            return JsonResponse({'service_id' : this_service_id})
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

## 초대코드 검색 & 랜덤 추출
@api_view(['GET'])
@permission_classes((AllowAny,))
def searchInvitation(request, keyword):
    ## 이 키워드에 맞는 Service 오브젝트 먼저 가져오기
    searched_service = Service.objects.filter(Q(service_kr__icontains=keyword) | Q(service_en__icontains=keyword) & Q(verified=True)).distinct()

    search_result = []
    ## 각각에 대한 Invitation random으로 1개씩 가져오기
    for i in range(0, len(searched_service)):
        this_invi = Invitation.objects.filter(service=searched_service[i]).order_by('?')[0]
        serializer = InvitationSerializer(this_invi)
        search_result.append(serializer.data)

    return JsonResponse(search_result, status=200, safe=False)

## 초대코드 등록을 위한 검색
@api_view(['GET'])
@permission_classes((AllowAny,))
def searchService(request, keyword):
    ## 이 키워드에 맞는 Service 오브젝트 먼저 가져오기
    searched_service = Service.objects.filter(Q(service_kr__icontains=keyword) | Q(service_en__icontains=keyword) & Q(verified=True)).distinct()

    search_result = []
    ## 각각에 대한 Invitation random으로 1개씩 가져오기
    for i in range(0, len(searched_service)):
        serializer = ServiceSerializer(searched_service[i])
        search_result.append(serializer.data)

    return JsonResponse(search_result, status=200, safe=False)

## 등록된 전체 서비스 조회
@api_view(['GET'])
@permission_classes((AllowAny,))
def getAllServices(request):
    all_services = Service.objects.filter(verified=True)

    result = []
    for i in range(0, len(all_services)):
        serializer = ServiceSerializer(all_services[i])
        result.append(serializer.data)

    return JsonResponse(result, status=200, safe=False)