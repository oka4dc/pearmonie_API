from rest_framework import permissions

class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Custom permission that allows:
    - Buyers to only view products.
    - Sellers to create, update, and delete products.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS (GET, HEAD, OPTIONS) are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True  # Buyers and Sellers can read (GET, HEAD, OPTIONS)

        # Only allow sellers to make changes (POST, PUT, PATCH, DELETE)
        return request.user.groups.filter(name='Sellers').exists()
