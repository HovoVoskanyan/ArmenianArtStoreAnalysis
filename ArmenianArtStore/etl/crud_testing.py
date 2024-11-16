from crud import create_user, get_user, update_user, delete_user
from database import get_db

db = next(get_db())
print("Database session initialized.")

# Create a User
new_user = create_user(db, device_type="Desktop", user_type="Admin")
print(f"Created User: {new_user}")

# Read the User
read_user = get_user(db, new_user.UserId)
print(f"Read User: {read_user}")

# Update the User
updated_user = update_user(db, new_user.UserId, device_type="Mobile", user_type="User")
print(f"Updated User: {updated_user}")

# Delete the User
deleted_user = delete_user(db, new_user.UserId)
print(f"Deleted User: {deleted_user}")
