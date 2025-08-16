import json

def create_task_json(task_id, train_data, test_data):
    task = {
        "train": train_data,
        "test": test_data
    }
    with open(f"task{task_id:03}.json", "w") as f:
        json.dump(task, f)

# task001
create_task_json(1,
    [{"input": [[0, 2], [3, 0]], "output": [[1, 2], [3, 1]]}],
    [{"input": [[0, 0], [0, 0]], "output": [[1, 1], [1, 1]]}]
)

# task002
create_task_json(2,
    [{"input": [[1, 2], [3, 4]], "output": [[2, 3], [4, 5]]}],
    [{"input": [[0, 0], [0, 0]], "output": [[1, 1], [1, 1]]}]
)

# task003
create_task_json(3,
    [{"input": [[1, 2], [3, 4]], "output": [[2, 4], [6, 8]]}],
    [{"input": [[0, 1], [2, 3]], "output": [[0, 2], [4, 6]]}]
)

import zipfile

with zipfile.ZipFile("submission.zip", "w") as zipf:
    zipf.write("task001.py")
    zipf.write("predict.py")  # Only if it exists
