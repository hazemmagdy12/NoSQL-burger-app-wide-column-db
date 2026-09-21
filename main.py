import time
from crud import setup_table, log_user_activity, get_user_history

def main():
    print("Starting Phase 3: Wide-Column DB Operations...\n")
    
    table = setup_table()
    
    print("\n--- Simulating User Activity ---")
    log_user_activity(table, user_id="user_123", action="view_item", burger_id="b1")
    
    time.sleep(1)
    
    log_user_activity(table, user_id="user_123", action="add_to_cart", burger_id="b1")
    
    print("\n--- Displaying User History ---")
    get_user_history(table, user_id="user_123")
    
    print("\n Phase 3 completed successfully!")

if __name__ == "__main__":
    main()