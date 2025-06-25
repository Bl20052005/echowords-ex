from django import forms
from django.http import JsonResponse, HttpResponseBadRequest

from core.models import *

# force_post decorator ensures request is POST
# otherwise reply with 403
def force_post(view):
    def _inner(request):
        if request.method == "POST":
            view(request)
        else:
            return HttpResponseBadRequest()
    return _inner

def response_fail(msg):
    return {"success": False, "error": msg}

class LoginForm(forms.Form):
    uname = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(label="Password", max_length=256)

@force_post
def auth_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        try:
            query = UserModel.objects.get(name=form.uname, pw=form.password)
            request.session["uid"] = query.uid
        except: pass
    return JSONResponse(response_fail("AUTH_INCORRECT"))

