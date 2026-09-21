from datetime import datetime, timezone
from database import db

TABLE_NAME = "user_activity"

def setup_table():
    try:
        table = db.create_table(
            TABLE_NAME,
            definition={
                "columns": {
                    "user_id": {"type": "text"},
                    "activity_time": {"type": "timestamp"},
                    "action": {"type": "text"},
                    "burger_id": {"type": "text"}
                },
                "primaryKey": {
                    "partitionBy": ["user_id"],
                    "partitionSort": {"activity_time": -1} 
                }
            }
        )
        print(f" Table '{TABLE_NAME}' created successfully!")
        return table
    except Exception:
        print(f" Table '{TABLE_NAME}' already exists. Fetching it...")
        return db.get_table(TABLE_NAME)

def log_user_activity(table, user_id, action, burger_id):
    table.insert_one({
        "user_id": user_id,
        "activity_time": datetime.now(timezone.utc),
        "action": action,
        "burger_id": burger_id
    })
    print(f" Logged action: '{action}' for user: '{user_id}'")

def get_user_history(table, user_id):
    print(f"\n Fetching history for '{user_id}':")
    cursor = table.find({"user_id": user_id})
    
    for row in cursor:
        print(f"- Time: {row['activity_time']}, Action: {row['action']}, Item: {row['burger_id']}")