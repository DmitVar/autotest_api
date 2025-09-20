import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, validator, EmailStr
from pydantic.alias_generators import to_camel

class BaseUserSchema(BaseModel):
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class UserSchema(BaseUserSchema):
    id: str

class CreateUserRequestSchema(BaseUserSchema):
    password: str

class CreateUserResponseSchema():
    user: UserSchema