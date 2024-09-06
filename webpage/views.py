from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def card(request):
    cards = []
    base_url = 'https://image.thepeople.co/uploads/images/contents/w1024/2024/03/gqwrPwkaj9O7pqBglQ5g.webp?x-image-process=style/lg-webp'
    
    for i in range(1, 101):
        image_url = f'{base_url}&{i}'
        card = {
            'image_url': image_url,
            'link': f'#card-{i}'
        }
        cards.append(card)

    context = {
        'cards': cards
    }
    return render(request, 'card.html', context)

def cardcolor(request):
    context = {
        'color': 'All',
    }

    if request.method == "GET" and request.GET.get('color') != None:
        context['color'] = request.GET.get('color')

    return render(request, 'cardcolor.html', context)

def form(request):
    return render(request, 'form.html')

@csrf_exempt
def submit_registration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # ตรวจสอบความถูกต้องของข้อมูล
            if not all([data.get('firstName'), data.get('lastName'), data.get('email'), 
                        data.get('address'), data.get('phone'), data.get('birthdate')]):
                return JsonResponse({'status': 'error', 'message': 'กรุณากรอกข้อมูลให้ครบถ้วน'})
            
            # ตรวจสอบรูปแบบอีเมล
            if '@' not in data['email']:
                return JsonResponse({'status': 'error', 'message': 'รูปแบบอีเมลไม่ถูกต้อง'})
            
            # ตรวจสอบความยาวของที่อยู่
            if len(data['address']) < 10:
                return JsonResponse({'status': 'error', 'message': 'ที่อยู่ต้องมีความยาวอย่างน้อย 10 ตัวอักษร'})
            
            # ตรวจสอบรูปแบบเบอร์โทรศัพท์
            if not data['phone'].isdigit() or len(data['phone']) != 10:
                return JsonResponse({'status': 'error', 'message': 'เบอร์โทรศัพท์ต้องเป็นตัวเลข 10 หลัก'})
            
            # ตรวจสอบวันเกิด
            try:
                birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d')
                if birthdate > datetime.now():
                    return JsonResponse({'status': 'error', 'message': 'วันเกิดไม่ถูกต้อง'})
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'รูปแบบวันเกิดไม่ถูกต้อง'})
            
            # บันทึกข้อมูลลงในฐานข้อมูล
            user = User(
                first_name=data['firstName'],
                last_name=data['lastName'],
                email=data['email'],
                address=data['address'],
                phone=data['phone'],
                birthdate=birthdate
            )
            user.save()
            
            return JsonResponse({'status': 'success', 'message': 'บันทึกข้อมูลเรียบร้อยแล้ว'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def forpage(request):
    context = {}
    lt = list(range(1, 101))

    first_names = ["Alan", "Marckris", "Khunpol", "Heart", "Jinwook", "Thai", "Nex", "Phutatchai", "Copper", "AA", "Jungt", "Peemwasu"]
    last_names = ["Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus", "Bus"]
    handles = ["IG: Alan.bus", "IG: Marckris.bus", "IG: Khunpol.bus", "IG: Heart.bus", "IG: Jinwook.bus", "IG: Thai.bus", "IG: Nex.bus", "IG: Phutatchai.bus", "IG: Copper.bus", "IG: AA.bus", "IG: Jungt.bus", "IG: Peemwasu.bus"]

    data = []
    for i in lt:
        first_name = first_names[(i - 1) % len(first_names)]
        last_name = last_names[(i - 1) % len(last_names)]
        handle = handles[(i - 1) % len(handles)]
        data.append({
            "id": i,
            "first_name": first_name,
            "last_name": last_name,
            "handle": handle
        })

    context["list"] = data

    return render(request, 'forpage.html', context)


