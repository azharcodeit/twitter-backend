from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import User
from .serializers import UserSerializer, PostSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def user_detail(request, pk):
    user = User.objects.get(pk=pk)

    serializer = UserSerializer(user, many=False)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def posts(request):
    posts = request.user.posts.all()

    print('user', request.user)
    print(posts)
    
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)