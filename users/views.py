import logging
from gc import get_objects
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from tutorial.quickstart.serializers import UserSerializer
from .permissions import IsAdminUserOrSuperuser



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Définir la requête pour récupérer tous les utilisateurs
    serializer_class = UserSerializer  # Spécifier le sérialiseur à utiliser pour cet ensemble de vues
    permission_classes = [IsAuthenticated, IsAdminUserOrSuperuser]

    # modifier le mot de passe de l'utilisateur
    @action(detail=True, methods=['POST'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('password')
        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({"status": "Mot de passe mis à jour"}, status=status.HTTP_200_OK)
        return Response({"error": "Mot de passe manquant"}, status=status.HTTP_400_BAD_REQUEST),


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = serializer.save()
        # user.set_password(request.data['password'])  # Hacher le mot de passe
        user.save()
        # Récupérer le rôle spécifié
        role = request.data.get('role')
        # Ajouter l'utilisateur au groupe correspondant
        if role == 'gestionnaire':
            group = Group.objects.get(name='Gestionnaire')
        elif role == 'vendeur':
            group = Group.objects.get(name='Vendeur')
        else:
            return Response({"error": "Role invalide"}, status=status.HTTP_400_BAD_REQUEST)
        user.groups.add(group)  # Ajouter l'utilisateur au groupe
        user.save()
        # Créer un token d'authentification pour l'utilisateur
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user, context={'request': request})
    return Response({'token': token.key, 'user': serializer.data})



@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def register_admin(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not (username and email and password):
        return Response(
            {"error": "Les champs 'username', 'email' et 'password' sont requis"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Créer un utilisateur admin
    admin_user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    return Response(
        {"message": f"Admin {admin_user.username} créé avec succès."},
        status=status.HTTP_201_CREATED
    )

@api_view(['POST'])
def admin_login(request):
    """
    Authentification d'un administrateur.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not (username and password):
        return Response(
            {"error": "Les champs 'username' et 'password' sont requis"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = get_object_or_404(User, username=username)

    if not user.check_password(password):
        return Response(
            {"error": "Nom d'utilisateur ou mot de passe incorrect"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not user.is_staff and not user.is_superuser:
        return Response(
            {"error": "L'utilisateur n'est pas un administrateur"},
            status=status.HTTP_403_FORBIDDEN
        )

    token, created = Token.objects.get_or_create(user=user)
    return Response({
        "token": token.key,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff
        }
    })

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])

def test_token(request):
    return Response("passed!")