# add_sample_user.py
from models.database import Session, User, init_db

# Initialize the database
init_db()

session = Session()

# Check if sample user exists
existing_user = session.query(User).filter_by(username="admin").first()
if not existing_user:
    sample_user = User(username="admin", password="admin123", role="manager")
    session.add(sample_user)
    session.commit()
    print("Sample user added.")
else:
    print("Sample user already exists.")
