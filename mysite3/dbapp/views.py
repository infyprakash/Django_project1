from django.shortcuts import render_to_response
from dbapp.models import Student,Department
from django.template import RequestContext

# Create your views here.
def index(request):
	context=RequestContext(request)
	department_list=Department.objects.all()
	context_dict={'departmentlists':department_list}
	return render_to_response('dbapp/index.html',context_dict,context)
def department(request,department_name_url):
	context=RequestContext(request)
	context_dict={'department_name':department_name_url}
	try:
		students=Student.objects.filter(dept_name__dept_name=department_name_url)
		context_dict['students']=students
	except Department.DoesNotExist:
		pass
	return render_to_response('dbapp/department.html',context_dict,context)
    