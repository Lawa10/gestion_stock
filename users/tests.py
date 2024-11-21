from django.test import TestCase

# Create your tests here.
#admin register
# url = http://127.0.0.1:8000/users/admin/register/
{
    "username": "admin_username",
    "email": "admin@example.com",
    "password": "secure_password"
}



# url = http://127.0.0.1:8000/users/admin/login/

{
    "username": "admin_username",
    "password": "secure_password"
}

# url = http://127.0.0.1:8000/users/create/

{
    "username": "user_username",
    "email": "user@example.com",
    "password": "secure_password",
    "role": "gestionnaire"
}


# url = http://127.0.0.1:8000/users/login/

{
    "username": "user_username",
    "password": "secure_password"
}


# url =  http://127.0.0.1:8000/users/{user_id}/set_password/

{
    "password": "new_secure_password"
}

