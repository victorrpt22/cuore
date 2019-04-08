from django.http        import (HttpResponse, JsonResponse)
from django.template    import loader
from .models            import Patient
import json

# Create your views here.
def index(request):
    all_patients = Patient.objects.order_by('-registered')
    template = loader.get_template('patients/index.html')
    context = {
        'all_patients': all_patients,
    }
    return HttpResponse(template.render(context, request))

def detail(request, patient_id):
    patient=Patient.objects.get(pk=patient_id)
    template = loader.get_template('patients/details.html')
    context = {
        'patient': patient
    }
    return HttpResponse(template.render(context, request))

def get_last_signals(request, patient_id):
    patient=Patient.objects.get(pk=patient_id)
    data=patient.logs_set.order_by('-inserted')[:20][::-1]
    arr=[]
    for i in data:
        arr.append(i.heart_rate)
    json_data = {'data': arr}
    return JsonResponse(json_data)