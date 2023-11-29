from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class BlockerView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, key=None):
        return Response({"detail": "ok"}, status=status.HTTP_200_OK)

    def post(self, request, key=None):
        return Response({"detail": "ok"}, status=status.HTTP_200_OK)
