# Password Managements and Session Managements

import os
from datetime import datetime, timedelta, timezone  # Needed for Token expiration times
from typing import Optional

# For password hashing
from passlib.context import CryptContext

# For creating/decoding JWTs (JSON Web Tokens)
from jose import jwt, JWTError



#--------------------------------------------------------------------------------------------------------------------------------------------

# 1. Managing Passwords

# Creating context for password hashing
password_context = CryptContext(schemes=["bcrypt"] , depracted = "auto")   # "bcrypt" - Industry Standard 

# Returns the hashed password
def hash_password(password: str):
    return password_context.hash(password)


# Verifies the password
def verify_password(input_password: str , hashed_password: str):
    return password_context.verify(input_password , hashed_password)

#--------------------------------------------------------------------------------------------------------------------------------------------


# 2. JWT Token Configuration