from django.contrib import messages


#helper functions for user input verification
#add functions here for user input (example bio)
class User_Verification():

    def __init__(self):
        super(User_Verification, self).__init__()

    #checks users inpput for bad strings or incorrect format
    #returns false if any issues arrise. add messages to display to users
    def signup_verify(request, username, email, password1, password2):
        if (User_Verification.check_username(request,username,'SignUpError') 
            and User_Verification.check_password(request,password1,password2,'SignUpError') 
            and User_Verification.check_email(request,email,'SignUpError')):
            return True
        return False

    #checks users inpput for bad strings or incorrect format
    #returns false if any issues arrise. add messages to display to users
    def login_verify(request, username, password):
        if (User_Verification.check_username(request,username,'LoginUpError') 
            and User_Verification.check_password(request,password,'','LoginUpError')):
            return True
        return False

    def check_username(request,username,pagetype):
        if not username:
            messages.error(request, 'Username is blank', extra_tags=pagetype)
        return True

    def check_password(request,password1, password2, pagetype):
        if not password1 and pagetype == 'LoginUpError':
            messages.error(request,'password is blank', extra_tags=pagetype)
        elif not password1 or not password2:
            messages.error(request,'password is blank', extra_tags=pagetype)
        elif not password1 == password2:
            messages.error(request,'password dont match', extra_tags=pagetype)
        return True

    def check_email(request,email,pagetype):
        if not email:
            messages.error(request, 'email is blank', extra_tags=pagetype)
        return True