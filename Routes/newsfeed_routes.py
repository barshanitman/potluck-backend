from fastapi import APIRouter,status,Depends
from schemas import UserSignup,LoginModel
from database import Session,engine
from models import *
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


