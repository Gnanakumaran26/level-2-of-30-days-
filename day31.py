import os
import shutil
from datetime import datetime

def backup_files(source_folder, backup_folder):
    # Create backup folder with date & time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination = os.path.join(backup_folder, f"backup_{timestamp}")
    os.makedirs(destination, exist_ok=True)
    
    try:
        shutil.copytree(source_folder, destination, dirs_exist_ok=True)
        print(f"✅ Backup completed! Files saved to: {destination}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def restore_backup(backup_folder, restore_folder):
    backups = [f for f in os.listdir(backup_folder) if f.startswith('backup_')]
    
    if not backups:
        print("⚠️ No backups found.")
        return
    
    print("Available backups:")
    for i, b in enumerate(backups):
        print(f"{i+1}. {b}")
    
    choice = int(input("Enter the number of the backup to restore: ")) - 1
    selected_backup = os.path.join(backup_folder, backups[choice])
    
    try:
        shutil.copytree(selected_backup, restore_folder, dirs_exist_ok=True)
        print(f"✅ Backup {backups[choice]} restored to {restore_folder}")
    except Exception as e:
        print(f"❌ Restore failed: {e}")

# Main function
if __name__ == "__main__":
    print("=== File Backup & Restore System ===")
    choice = input("Do you want to (B)ackup or (R)estore? ").lower()

    if choice == 'b':
        source = input("Enter source folder path: ")
        destination = input("Enter backup folder path: ")
        backup_files(source, destination)
    elif choice == 'r':
        backup_folder = input("Enter backup folder path: ")
        restore_folder = input("Enter restore folder path: ")
        restore_backup(backup_folder, restore_folder)
    else:
        print("Invalid option. Please select 'B' or 'R'.")
