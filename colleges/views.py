from django.shortcuts import render_to_response
from colleges.models import School
from django.contrib.syndication.views import Feed

def list_schools(request):
  schools = School.objects.order_by('id')[:5]
  return render_to_response('colleges/schools.html', {'schools': schools})