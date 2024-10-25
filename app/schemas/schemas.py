from typing import List, Optional
from pydantic import BaseModel


class SpyCatBase(BaseModel):
    name: str
    years_of_experience: int
    breed: str
    salary: int


class SpyCatCreate(SpyCatBase):
    pass


class SpyCatUpdate(BaseModel):
    name: Optional[str] = None
    years_of_experience: Optional[int] = None
    breed: Optional[str] = None
    salary: Optional[int] = None


class SpyCatResponse(SpyCatBase):
    id: int

    class Config:
        from_attributes = True


class MissionBase(BaseModel):
    cat_id: int
    complete: Optional[bool] = False


class MissionCreate(MissionBase):
    targets: List[str]


class MissionUpdate(BaseModel):
    cat_id: Optional[int] = None
    complete: Optional[bool] = None
    targets: Optional[List[str]] = None


class MissionResponse(MissionBase):
    id: int

    class Config:
        from_attributes = True


class TargetBase(BaseModel):
    name: str
    country: Optional[str]
    notes: Optional[str] = None
    complete: Optional[bool] = False


class TargetCreate(TargetBase):
    mission_id: int


class TargetResponse(TargetBase):
    id: int

    class Config:
        from_attributes = True
