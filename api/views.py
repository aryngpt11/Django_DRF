from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse
# Model Object - Single Student Data

def student_detail(request, pk):#pk=we pass the id in the url
    stu=Student.objects.get(id=pk)  #Complex Data
    serializer=StudentSerializer(stu) #Converting in python native datatype
    #now covert it into json format then we use json_renderer
    
    json_data=JSONRenderer().render(serializer.data)
    #now we get data in form of json then we have to send this data as response to the client 
    
    return HttpResponse(json_data,content_type='application/json')
    #or
    #return JsonResponse(serializer.data)
# QuerySet - All Student Data

def student_list(request):
    stu=Student.objects.all()  #Complex Data
    serializer=StudentSerializer(stu, many=True) #Converting in python native datatype
    #now covert it into json format then we use json_renderer
    #json_data=JSONRenderer().render(serializer.data)
    #now we get data in form of json then we have to send this data as response to the client 
    #return HttpResponse(json_data,content_type='application/json')

    #or
    return JsonResponse(serializer.data,safe=False)