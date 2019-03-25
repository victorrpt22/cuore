from django.http        import HttpResponse
from django.template    import loader
from .models            import Patient

# Create your views here.
def index(request):
    all_patients = Patient.objects.order_by('-registered')
    template = loader.get_template('patients/index.html')
    context = {
        'all_patients': all_patients,
    }
    return HttpResponse(template.render(context, request))

def detail(request, patient_id):
    response="You're looking at patient %s."
    return HttpResponse(response % patient_id)