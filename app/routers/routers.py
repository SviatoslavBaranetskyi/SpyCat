from app.db.database import SessionLocal
from app.schemas.schemas import *
from app.services.crud import *

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/cats/", response_model=SpyCatResponse)
def add_spy_cat(spy_cat: SpyCatCreate, db: Session = Depends(get_db)):
    return create_spy_cat(db=db, spy_cat=spy_cat)


@router.get("/cats/", response_model=List[SpyCatResponse])
def list_spy_cats(db: Session = Depends(get_db)):
    return get_spy_cats(db=db)


@router.get("/cats/{spy_cat_id}", response_model=SpyCatResponse)
def read_spy_cat(spy_cat_id: int, db: Session = Depends(get_db)):
    spy_cat = get_spy_cat(db=db, spy_cat_id=spy_cat_id)
    if spy_cat is None:
        raise HTTPException(status_code=404, detail="Spy cat not found")
    return spy_cat


@router.put("/cats/{spy_cat_id}", response_model=SpyCatResponse)
def update_spy_cat(spy_cat_id: int, spy_cat_update: SpyCatUpdate, db: Session = Depends(get_db)):
    spy_cat = update_spy_cat_in_db(db=db, spy_cat_id=spy_cat_id, spy_cat_update=spy_cat_update)
    if spy_cat is None:
        raise HTTPException(status_code=404, detail="Spy cat not found")
    return spy_cat


@router.delete("/cats/{spy_cat_id}")
def remove_spy_cat(spy_cat_id: int, db: Session = Depends(get_db)):
    if not delete_spy_cat(db=db, spy_cat_id=spy_cat_id):
        raise HTTPException(status_code=404, detail="Spy cat not found")
    return {"detail": "Spy cat removed"}


# Missions Endpoints
@router.post("/missions/", response_model=MissionResponse)
def add_mission(mission: MissionCreate, db: Session = Depends(get_db)):
    return create_mission(db=db, mission=mission)


@router.get("/missions/", response_model=List[MissionResponse])
def list_missions(db: Session = Depends(get_db)):
    return get_missions(db=db)


@router.get("/missions/{mission_id}", response_model=MissionResponse)
def read_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = get_mission(db=db, mission_id=mission_id)
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission


@router.put("/missions/{mission_id}", response_model=MissionResponse)
def update_mission_endpoint(
        mission_id: int,
        mission_update: MissionUpdate,
        db: Session = Depends(get_db)
):
    return update_mission(db=db, mission_id=mission_id, mission_update=mission_update)


@router.delete("/missions/{mission_id}")
def remove_mission(mission_id: int, db: Session = Depends(get_db)):
    if not delete_mission(db=db, mission_id=mission_id):
        raise HTTPException(status_code=404, detail="Mission not found")
    return {"detail": "Mission removed"}


# Targets Endpoints
@router.post("/targets/", response_model=TargetResponse)
def add_target(target: TargetCreate, db: Session = Depends(get_db)):
    return create_target(db=db, target=target)


@router.get("/targets/", response_model=List[TargetResponse])
def list_targets(db: Session = Depends(get_db)):
    return get_targets(db=db)


@router.put("/targets/{target_id}", response_model=TargetResponse)
def edit_target(target_id: int, target: TargetCreate, db: Session = Depends(get_db)):
    return update_target(db=db, target_id=target_id, target=target)


@router.delete("/targets/{target_id}")
def remove_target(target_id: int, db: Session = Depends(get_db)):
    if not delete_target(db=db, target_id=target_id):
        raise HTTPException(status_code=404, detail="Target not found")
    return {"detail": "Target removed"}
