from pydantic import BaseModel


class BaseClass(BaseModel):
    class Config:
        validate_assignment = True
