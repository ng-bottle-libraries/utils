from re import match


def is_email(email):
    return bool(match("^[a-zA-Z0-9._-]+\@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$", email))
