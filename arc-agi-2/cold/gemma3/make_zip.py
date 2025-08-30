import os
import zipfile

# Directory where this script and target files live
BASE_DIR = os.path.dirname(__file__)

# Files to include (relative to BASE_DIR)
FILES_TO_ZIP = [
    "evaluator.py",
    "generate-tasks.py",
    "task001.py",
    "task002.py",
    "task003.py",
    "make_zip.py",
    "model_runner.py",
    "solution-writer.py"
]

# Output zip file path (in parent directory)
ZIP_PATH = os.path.join(BASE_DIR, "..", "arc_tasks.zip")

with zipfile.ZipFile(ZIP_PATH, "w") as zipf:
    for filename in FILES_TO_ZIP:
        full_path = os.path.join(BASE_DIR, filename)
        if os.path.exists(full_path):
            zipf.write(full_path, arcname=filename)
            print(f"✅ Added: {filename}")
        else:
            print(f"⚠️ File not found — skipping: {filename}")

print(f"\n📦 Zip created at: {os.path.abspath(ZIP_PATH)}")
