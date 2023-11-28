import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash
from database import Base, engine 


from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True, autoincrement=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)


# class Lead(_database.Base):
#     __tablename__ = "leads"
#     id = _sql.Column(_sql.Integer, primary_key=True, index=True)
#     owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
#     first_name = _sql.Column(_sql.String, index=True)
#     last_name = _sql.Column(_sql.String, index=True)
#     email = _sql.Column(_sql.String, index=True)
#     company = _sql.Column(_sql.String, index=True, default="")
#     note = _sql.Column(_sql.String, default="")
#     date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
#     date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
#     owner = _orm.relationship("User", back_populates="leads")
#     from_attributes = True
 
Base.metadata.create_all(bind=engine)
