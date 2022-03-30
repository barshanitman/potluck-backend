from pydantic import BaseModel
from typing import Optional

class UserSignup(BaseModel):
    firstName:str
    lastName:str
    email:str
    dateOfBirth:str
    address:str
    password:str
    paymentstatus:bool
    subscriptiontypeid:Optional[int]

class Settings(BaseModel):
    authjwt_secret_key: str='a0f9f490812e6014dfc4810ab623fdbea164128f346510e008dcdeffafdfeb65'

class LoginModel(BaseModel):
    email: str 
    password: str

class SupplierSignup(BaseModel):
    name: str 
    address: str 
    state: str 
    anb:int
    postcode: int 
    

