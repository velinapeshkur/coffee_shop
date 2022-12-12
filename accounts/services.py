import avinit
from django.http import HttpRequest
from accounts.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from typing import Literal


AVATAR_COLORS = [
        "#F8BB05",
    ]

SMALL_AVATAR_CONFIG = {
        "width": "42",
        "height": "42",
        "radius": "21",
        "font-size": "15",
        "font-weight": "bold",
    }

LARGE_AVATAR_CONFIG = {
        "width": "120",
        "height": "120",
        "radius": "60",
        "font-size": "45",
        "font-weight": "bold",
    }

def get_user_avatar(request: HttpRequest, full_name: str) -> None:
    """
    Generates simple svg avatar with user's initials and saves it in session.
    """
    request.session["avatar"] = avinit.get_svg_avatar(
       full_name, colors=AVATAR_COLORS, **SMALL_AVATAR_CONFIG
    )
    request.session["large_avatar"] = avinit.get_svg_avatar(
        full_name, colors=AVATAR_COLORS, **LARGE_AVATAR_CONFIG
    )


def logout_check(user: User) -> Literal[False]:
    """
    Checks if user is not authenticated.
    """
    return user.is_anonymous



def user_login(request: HttpRequest, login_data: dict) -> None:
    username = login_data.get("username")
    password = login_data.get("password")
    user = authenticate(username=username, password=password)

    if user:
        login(
            request, user, backend="django.contrib.auth.backends.ModelBackend"
        )
        get_user_avatar(request, full_name = user.get_full_name())
