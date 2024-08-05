from pydantic import BaseModel, EmailStr


class RegisterRequestSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
