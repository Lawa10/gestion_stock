from rest_framework.permissions import BasePermission


class IsAdminUserOrSuperuser(BasePermission):
    """
    Permet l'accès uniquement aux utilisateurs administrateurs ou superutilisateurs.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)
