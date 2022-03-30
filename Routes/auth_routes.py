from fastapi import APIRouter,status,Depends
from schemas import SupplierSignup, UserSignup,LoginModel
from database import Session,engine
from models import *
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(prefix='/auth',tags=['auth'])

session = Session(bind=engine)

@auth_router.post('/users/signup')
async def signup(request:UserSignup):
    db_email = session.query(Users).filter(Users.email==request.email).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail='User already exists')

    new_user = Users(
        firstname=request.firstName,
        lastname=request.lastName,
        email=request.email,
        dateofbirth = request.dateOfBirth,
        address=request.address,
        password=generate_password_hash(request.password),
        paymentstatus=0,
        subscriptiontypeid=4
    )

    session.add(new_user)
    session.commit()

    return {'Message':'User created'}

@auth_router.post('/users/login')
async def login(request:LoginModel,Authorize:AuthJWT=Depends()) -> None:
    db_user = session.query(Users).filter(Users.email == request.email).first()
    if db_user and check_password_hash(db_user.password,request.password):
        access_token = Authorize.create_access_token(subject=db_user.email)
        refresh_token = Authorize.create_refresh_token(subject=db_user.email)

        response = {
             'access_token':access_token,
             'refresh_token':refresh_token}

        return jsonable_encoder(response)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Invalid email or password')

@auth_router.post('/suppliers/signup')
async def login(request:SupplierSignup):
    db_anb = session.query(Branch).filter(Branch.anb == request.anb).first()
    if db_anb is not None:
        return  HTTPException(status_code=status.HTTP_400_BAD_REQUEST,details='Supplier already exists')
    new_branch = Branch(
        name=request.name,
        anb=request.anb,
        address=request.address,
        state=request.state,
        postcode=request.postcode
    )
    session.add(new_branch)
    session.commit()
    return {'Message':'Supplier Created'}
