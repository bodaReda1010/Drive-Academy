from . models import Account

def get_profile(request , profile = None):
    if request.user.is_authenticated:
        profile = Account.objects.get(user=request.user)
    return {'profile': profile,}