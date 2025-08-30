import json

def create_task_json(task_id, train_data, test_data, metadata):
    task = {
        "train": train_data,
        "test": test_data,
        "metadata": metadata
    }
    with open(f"task{task_id:03}.json", "w") as f:
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
with zipfile.ZipFile("submission.zip", "w") as zipf:
    zipf.write("task001.py")
    zipf.write("task002.py")
    zipf.write("task003.py")
    zipf.write("model_runner.py")
    zipf.write("generate-tasks.py")
    zipf.write("evalutor.py")
    try:
        zipf.write("predict.py")  # Optional
    except FileNotFoundError:
        print("predict.py not found — skipping.")
























