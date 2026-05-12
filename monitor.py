import os
import json
import hashlib
import time

# Folders to monitor
MONITOR_FOLDERS = [

    "monitor_folder",

    "C:/Users/hp/Documents",

    "C:/Users/hp/Desktop"

]

# Files
HASH_FILE = "hashes.json"
LOG_FILE = "logs.txt"

# Create folders if missing
for folder in MONITOR_FOLDERS:

    if not os.path.exists(folder):

        os.makedirs(folder)

# =========================
# Generate SHA256 Hash
# =========================

def calculate_hash(filepath):

    sha256 = hashlib.sha256()

    try:

        with open(filepath, "rb") as f:

            while chunk := f.read(4096):

                sha256.update(chunk)

        return sha256.hexdigest()

    except:

        return None

# =========================
# Load Existing Hashes
# =========================

def load_hashes():

    if os.path.exists(HASH_FILE):

        with open(HASH_FILE, "r") as f:

            return json.load(f)

    return {}

# =========================
# Save Hashes
# =========================

def save_hashes(hashes):

    with open(HASH_FILE, "w") as f:

        json.dump(hashes, f, indent=4)

# =========================
# Write Logs
# =========================

def write_log(message):

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp}] {message}\n"

    with open(LOG_FILE, "a") as f:

        f.write(log_entry)

    print(log_entry)

# =========================
# Main Monitoring Function
# =========================

def monitor_files():

    old_hashes = load_hashes()

    current_hashes = {}

    for folder in MONITOR_FOLDERS:

        for root, dirs, files in os.walk(folder):

            for file in files:

                filepath = os.path.join(root, file)

                file_hash = calculate_hash(filepath)

                if file_hash:

                    current_hashes[filepath] = file_hash

                    # New File
                    if filepath not in old_hashes:

                        write_log(f"[NEW FILE] {filepath}")

                    # Modified File
                    elif old_hashes[filepath] != file_hash:

                        write_log(f"[MODIFIED] {filepath}")

    # Deleted Files
    for filepath in old_hashes:

        if filepath not in current_hashes:

            write_log(f"[DELETED] {filepath}")

    save_hashes(current_hashes)

# =========================
# Start Monitoring
# =========================

print("\n[ SecureWatch Monitoring Started ]\n")

while True:

    monitor_files()

    time.sleep(5)