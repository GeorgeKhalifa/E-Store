#Added by me
from App1.models import UserInfo
from django.contrib.auth import authenticate
def add_variable_to_context(request):
    if(request.user.is_authenticated and not request.user.is_superuser):
        actual_user = UserInfo.objects.filter(user = request.user)[0]
        firstname = request.user.first_name
        lastname = request.user.last_name
        if actual_user.BuyerOrSeller == 'seller':
            sellerflag = True
        else:
            sellerflag = False
    else:
        sellerflag = False
        firstname = ""
        lastname = ""
    return {
        'sellerflag': sellerflag, 'firstname': firstname, 'lastname': lastname
    }
