import json
import zipfile
from pathlib import Path

# 📁 Base directory resolution
BASE_DIR = Path(__file__).parent.resolve()

def create_task_json(task_id, train_data, test_data, metadata):
    task = {
        "train": train_data,
        "test": test_data,
        "metadata": metadata
    }
    task_file = BASE_DIR / f"task{task_id:03}.json"
    with open(task_file, "w") as f:
        json.dump(task, f, indent=2)

# 🔧 Task 001: Grid inversion
create_task_json(
    1,
    train_data=[
        {"input": [[0, 2], [3, 0]], "output": [[1, 2], [3, 1]]},
        {"input": [[0, 0], [0, 0]], "output": [[1, 1], [1, 1]]}
    ],
    test_data=[],
    metadata={
        "task_id": "task001",
        "description": "Invert 0s to 1s, leave others unchanged",
        "source": "Gemma3 ARC-style framework",
        "difficulty": "easy"
    }
)

# 🔧 Task 002: Increment each cell
create_task_json(
    2,
    train_data=[
        {"input": [[1, 2], [3, 4]], "output": [[2, 3], [4, 5]]},
        {"input": [[0, 0], [0, 0]], "output": [[1, 1], [1, 1]]}
    ],
    test_data=[],
    metadata={
        "task_id": "task002",
        "description": "Add 1 to each cell",
        "source": "Gemma3 ARC-style framework",
        "difficulty": "easy"
    }
)

# 🔧 Task 003: Multiply each cell by 2
create_task_json(
    3,
    train_data=[
        {"input": [[1, 2], [3, 4]], "output": [[2, 4], [6, 8]]},
        {"input": [[0, 1], [2, 3]], "output": [[0, 2], [4, 6]]}
    ],
    test_data=[],
    metadata={
        "task_id": "task003",
        "description": "Double each cell value",
        "source": "Gemma3 ARC-style framework",
        "difficulty": "easy"
    }
)

# 🗜️ Package submission files
files_to_zip = [
    "task001.py",
    "task002.py",
    "task003.py",
    "model_runner.py",
    "generate-tasks.py",
    "evaluator.py",
    "evaluator_batch.py",
    "solution_writer.py",
    "batch_writer.py"  # Optional
]

with zipfile.ZipFile(BASE_DIR / "submission.zip", "w") as zipf:
    for filename in files_to_zip:
        file_path = BASE_DIR / filename
        if file_path.exists():
            zipf.write(file_path, arcname=filename)
        else:
            print(f"{filename} not found — skipping.")






