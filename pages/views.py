# Create your views here.
# views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from pages.serializer import PageSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_page(request):
    serializer = PageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data["user_id"] = request.user.id
        page = serializer.save()
        return Response({"message": "Page created successfully", "page_id": page.id})
    else:
        return Response({"error": "Invalid data", "details": serializer.errors}, status=400)
