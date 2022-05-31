from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse

SERVER_VERSION = "0.0.1"

class AboutView(View):
    def get(self, request:HttpRequest):
        template_name = "about/index.html"
        context = {
            "user": request.user.username,
            "server_version": SERVER_VERSION
        }
        return render(
            request,
            template_name=template_name,
            context=context
        )


