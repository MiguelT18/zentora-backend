from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional, Dict, Any


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class ResendConfirmation(BaseModel):
    type: Literal["signup", "email_change", "phone_change", "sms"]
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    options: Optional[Dict[str, Any]] = Field(default_factory=dict)
