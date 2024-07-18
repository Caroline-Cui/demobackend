import json

from rest_framework.views import APIView

from backend.my_profile import get_profile_name, get_email_addr, set_email_addr, set_profile_name

from rest_framework import status
from rest_framework.response import Response


class MyProfile(APIView):
    def get(self, request):
        info = {
            'name': get_profile_name(),
            'email': get_email_addr(),
        }
        return Response(info, status=status.HTTP_200_OK)

    def post(self, request):
        new_name = request.data.get('name')
        new_email = request.data.get('email')
        if new_name :
            set_profile_name(new_name)
        if new_email:
            set_email_addr(new_email)

        return Response()

