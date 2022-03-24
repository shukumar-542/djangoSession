from email.policy import default
from django.shortcuts import render,HttpResponse

# Create your views here.


#PAGE COUNTER

def home(request):
      ct  = request.session.get('count',0)
      newCount = ct +1
      request.session['count'] = newCount
      return render(request, 'student/home.html', {'count':newCount})

def setsession(request):
      request.session['name'] = 'shukumar'
      # request.session.set_expiry(600) 
      return render(request,'student/setsession.html')

def getsession(request):
      if 'name' in  request.session:
            name =request.session['name']

            keys = request.session.keys()
            items = request.session.items()
            request.session.modified= True
            return render(request,'student/getsession.html',{'name':name, 'keys':keys,'items':items})
      else:
            return HttpResponse('Your session has been expired...')

def delsession(request):

      request.session.flush()
      request.session.clear_expired()
      # if 'name' in request.session:
      #       del request.session['name']
      return render(request, 'student/delsession.html')

