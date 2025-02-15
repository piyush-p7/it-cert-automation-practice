#!/usr/bin/env python3
import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen.
    if len(username) < minlen:
        return "Username must not be less than {} character.".format(minlen)
    # Usernames can only use letters, numbers, dots and underscores.
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a symbol.
    if username[0].isalpha():
        return False
    return True



