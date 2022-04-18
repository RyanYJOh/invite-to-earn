from django.shortcuts import render
from main.models import Service, Invitation

def uploadServices(request):
    list__service_kr = [
        "퍼블리"	,
        "퍼블리카"	,
        "퍼블리시모"	,
        "글램"	,
        "애플"	,
        "틴더"	,
        "틴더앱"	,
        "파인애플"	,
        "커리어리"	,
        "위하이어"	,
        "도미노"	,
        "블라인드"	,
        "미트리 닭가슴살"	,
        "지니 뮤직"	,
        "빗썸"	,
        "코인원"	
    ]
    list__service_en = [
        "Publy"	,
        "Publica"	,
        "Publissimo"	,
        "Glam"	,
        "Apple"	,
        "Tinder"	,
        "Tinerapp"	,
        "Pineapple"	,
        "Careerly"	,
        "Wehire"	,
        "Domino"	,
        "Blind"	,
        "Metree"	,
        "Genie music"	,
        "Bithumb"	,
        "Coinone"	
    ]
    list__logo_img = [
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	,
        "https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/30m2/image/Oa4RLziCKJAb78eR46fdiivEu5c.jpg"	
    ]
    list__verified = [
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	,
        True	
    ]

    for i in range(0, len(list__service_kr)):
        Service.objects.create(
            service_kr = list__service_kr[i],
            service_en = list__service_en[i],
            logo_img = list__logo_img[i],
            verified = list__verified[i]
        )
