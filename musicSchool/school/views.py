from django.shortcuts import render

from .models import Teacher
from django.contrib.auth import authenticate



def index(request):
    return render(
        request, 
        'index.html',
        {
            'posts': Teacher.objects.all(),
        }    
    )

#class MyprojectLoginView(LoginView):
#    template_name = 'login.html'
#    form_class = AuthUserForm
#    success_url = reverse_lazy('edit_page')
#    def get_success_url(self):
#        return self.success_url
