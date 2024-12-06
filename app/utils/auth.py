import jwt
from fastapi import HTTPException
import os

environment = os.getenv("ENVIRONMENT", "development")
JWT_SECRET = "bUqIEakocsDAsGLQ0hhkLDSulcmChoCjqSTtPeIno8kwsscgf3BmdV/Xwl6oZIZuyG77x6jP3Zeci93mVcNz4g==" if environment == "development" else "ZESwCG552GZv2SnHzL6ZEkDIrVs/M++SgjF3urCCsu7UNWKnv4AuSdCdQ/FW8j0zX0pF0Jv3Z3sLmaQaU7A4Fw=="

def is_authenticated(authorization: str):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header format")
    token = authorization.split(" ")[1]
    
    try:
        decoded_token = jwt.decode(token, JWT_SECRET , algorithms=["HS256"], audience="authenticated")
        isAuth = decoded_token['aud'] == 'authenticated'
        return isAuth
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")