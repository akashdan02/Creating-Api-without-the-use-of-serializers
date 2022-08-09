from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import RotaryclubVolunteerList
import json
from django.http import HttpResponse
# Create your views here.



class Volunteer(View):
    def get(self,request):
        volunteer_name = list(RotaryclubVolunteerList.objects.values())
        return JsonResponse(volunteer_name,safe=False)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Volunteer,self).dispatch(request,*args,*kwargs)

    def post(self,request):
        data = request.body.decode('utf8')
        data =json.loads(data)
        try:
            new_volunteer = RotaryclubVolunteerList(volunteer_name =data["volunteer_name"], past_socialwork=data["past_socialwork"],age=data["age"])
            new_volunteer.save()
        except:
            return JsonResponse({"error": "not a valid data"}, safe = False)

class VolunteerDetail(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VolunteerDetail, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        volunteer_list = {"volunteer": list(RotaryclubVolunteerList.objects.filter(pk=pk).values())}
        return JsonResponse(volunteer_list, safe=False)

    def put(self, request, pk):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_volunteer = RotaryclubVolunteerList.objects.get(pk=pk)
            data_key=list(data.keys())
            for key in data_key:
                if key =="volunteer_name":
                    new_volunteer.volunteer_name = data[key]
                if key =="past_socialwork":
                    new_volunteer.past_socialwork = data[key]
                if key =="age":
                    new_volunteer.age=data[key]
                new_volunteer.save()
                return JsonResponse({"updated": data}, safe=False)
        except RotaryclubVolunteerList.DoesNotExist:
            return JsonResponse({"error": "Volunteer having primary key does not exist"}, safe=False)

        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            new_volunteer = RotaryclubVolunteerList.objects.get(pk=pk)
            new_volunteer.delete()
            return JsonResponse({"deleted": True}, safe=False)
        except:
            return JsonResponse({"error": "not a valid primary key"}, safe=False)