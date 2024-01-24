import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Mission


@csrf_exempt
def mission(request: HttpRequest, mission_id: int | None=None):
    if request.method == 'POST':
        mission_json = json.loads(request.body.decode('utf8'))
        mission = Mission.from_json(mission_json, mission_id)
        if mission.is_valid():
            mission.accepted = True
            mission.save()
            return JsonResponse({'status': 'accepted', 'data': mission.to_json()}, status=201)
        else:
            mission.save()
            data = {
                'status': 'rejected', 
                'reason': mission.reject_reason, 
                'data': mission.to_json(),
                }
            return JsonResponse(data, status=201)
    
    if request.method == 'GET':
        if mission_id:
            mission = Mission.objects.get(pk=mission_id)
            if request.headers.get('Accept') == 'application/json':
                return JsonResponse({'mission': mission.to_json()})
            elif request.headers.get('Accept') == 'text/csv':
                response = HttpResponse(mission.to_csv(), content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="mission.csv"'
                return response
            else:
                return JsonResponse({'error': 'bad content type'}, status=400)
        
        missions = Mission.objects.all()
        return JsonResponse({'missions': [mission.to_json() for mission in missions]})
    
    if request.method == 'DELETE':
        if not mission_id:
            return JsonResponse({'error': 'mission_id required'}, status=400)
        Mission.objects.filter(id=mission_id).delete()
        return JsonResponse({'status': 'deleted'})
    
    return JsonResponse({'error': 'bad request'}, status=400)