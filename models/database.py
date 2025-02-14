# models/database.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(20))  # e.g., receptionist, manager
    reservations = relationship("Reservation", back_populates="user")

# Room model
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    room_number = Column(String(10), unique=True, nullable=False)
    type = Column(String(50))
    status = Column(String(20))  # e.g., available, occupied
    reservations = relationship("Reservation", back_populates="room")

# Reservation model
class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    check_in = Column(Date)
    check_out = Column(Date)
    user = relationship("User", back_populates="reservations")
    room = relationship("Room", back_populates="reservations")

# Create engine and session
engine = create_engine('sqlite:///hotel_app.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)  # Create tables if they don't exist
