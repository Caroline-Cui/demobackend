_profile_name = "Caroline"
_email_addr = "CarolineCui99@gmail.com"


def set_profile_name(new_profile_name):
    global _profile_name
    _profile_name = new_profile_name


def set_email_addr(new_email_addr):
    global _email_addr
    _email_addr = new_email_addr

def get_profile_name():
    return _profile_name

def get_email_addr():
    return _email_addr