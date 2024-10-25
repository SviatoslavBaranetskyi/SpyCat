from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import *
from app.schemas.schemas import *


# CRUD for SpyCat
def create_spy_cat(db: Session, spy_cat: SpyCatCreate) -> SpyCatResponse:
    db_spy_cat = SpyCat(**spy_cat.dict())
    db.add(db_spy_cat)
    db.commit()
    db.refresh(db_spy_cat)
    return SpyCatResponse.from_orm(db_spy_cat)


def get_spy_cat(db: Session, spy_cat_id: int) -> Optional[SpyCatResponse]:
    return db.query(SpyCat).filter(SpyCat.id == spy_cat_id).first()


def get_spy_cats(db: Session) -> List[SpyCatResponse]:
    return [SpyCatResponse.from_orm(cat) for cat in db.query(SpyCat).all()]


def update_spy_cat_in_db(db: Session, spy_cat_id: int, spy_cat_update: SpyCatUpdate) -> Optional[SpyCatResponse]:
    db_spy_cat = db.query(SpyCat).filter(SpyCat.id == spy_cat_id).first()
    if db_spy_cat:
        if spy_cat_update.name is not None:
            db_spy_cat.name = spy_cat_update.name
        if spy_cat_update.years_of_experience is not None:
            db_spy_cat.years_of_experience = spy_cat_update.years_of_experience
        if spy_cat_update.breed is not None:
            db_spy_cat.breed = spy_cat_update.breed
        if spy_cat_update.salary is not None:
            db_spy_cat.salary = spy_cat_update.salary
        db.commit()
        db.refresh(db_spy_cat)
        return SpyCatResponse.from_orm(db_spy_cat)
    return None


def delete_spy_cat(db: Session, spy_cat_id: int) -> bool:
    db_spy_cat = db.query(SpyCat).filter(SpyCat.id == spy_cat_id).first()
    if db_spy_cat:
        db.delete(db_spy_cat)
        db.commit()
        return True
    return False


# CRUD for Mission
def create_mission(db: Session, mission: MissionCreate) -> MissionResponse:
    db_mission = Mission(cat_id=mission.cat_id, complete=mission.complete)

    for target_name in mission.targets:
        db_target = Target(name=target_name)
        db_mission.targets.append(db_target)

    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return MissionResponse.from_orm(db_mission)


def get_mission(db: Session, mission_id: int) -> Optional[MissionResponse]:
    return db.query(Mission).filter(Mission.id == mission_id).first()


def get_missions(db: Session) -> List[MissionResponse]:
    return [MissionResponse.from_orm(mission) for mission in db.query(Mission).all()]


def update_mission(db: Session, mission_id: int, mission_update: MissionUpdate) -> MissionResponse:
    db_mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not db_mission:
        raise HTTPException(status_code=404, detail="Mission not found")

    if mission_update.cat_id is not None:
        db_mission.cat_id = mission_update.cat_id
    if mission_update.complete is not None:
        db_mission.complete = mission_update.complete

    if mission_update.targets is not None:
        db_mission.targets.clear()

        for target_name in mission_update.targets:
            db_target = Target(name=target_name)
            db_mission.targets.append(db_target)

    db.commit()
    db.refresh(db_mission)
    return MissionResponse.from_orm(db_mission)


def delete_mission(db: Session, mission_id: int) -> bool:
    db_mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if db_mission:
        db.delete(db_mission)
        db.commit()
        return True
    return False


# CRUD for Target
def create_target(db: Session, target: TargetCreate) -> TargetResponse:
    db_target = Target(**target.dict())
    db.add(db_target)
    db.commit()
    db.refresh(db_target)
    return TargetResponse.from_orm(db_target)


def get_target(db: Session, target_id: int) -> Optional[TargetResponse]:
    return db.query(Target).filter(Target.id == target_id).first()


def get_targets(db: Session) -> List[TargetResponse]:
    targets = db.query(Target).all()
    for target in targets:
        if target.country is None:
            print(f"Target ID: {target.id} has NULL country")
    return [TargetResponse.from_orm(target) for target in targets]


def update_target(db: Session, target_id: int, target: TargetCreate) -> TargetResponse:
    db_target = db.query(Target).filter(Target.id == target_id).first()

    if not db_target:
        raise HTTPException(status_code=404, detail="Target not found")

    db_target.name = target.name
    db_target.country = target.country
    db_target.notes = target.notes
    db_target.complete = target.complete
    db_target.mission_id = target.mission_id

    db.commit()
    db.refresh(db_target)
    return TargetResponse.from_orm(db_target)


def delete_target(db: Session, target_id: int) -> bool:
    db_target = db.query(Target).filter(Target.id == target_id).first()
    if db_target:
        db.delete(db_target)
        db.commit()
        return True
    return False

