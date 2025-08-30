def p(input_grid):
    """
    Transformation: set cell to 1 if any cell in its row or column 
is 1.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    row_flags = [any(input_grid[r]) for r in range(rows)]
    col_flags = [any(input_grid[r][c] for r in range(rows)) for c in 
range(cols)]

    return [
        [1 if row_flags[r] or col_flags[c] else 0 for c in range
(cols)]
        for r in range(rows)
    ]

def get_task():
    """
    Returns a sample ARC-style task dictionary.
    """
    return {
        "train": [
            {"input": [[1, 0], [0, 1]], "output": [[1, 1], [1, 1]]}
        ],
        "test": [
            {"input": [[0, 0], [0, 0]], "output": [[0, 0], [0, 0]]}
        ],
        "metadata": {
            "task_id": "task003",
            "description": "Grid OR operation — output is 1 if any 
cell in row or column is 1",
            "source": "Gemma3 ARC-style framework",
            "difficulty": "medium"
        }
    }

def main():
    """
    Runs evaluation on train and test samples using p().
    """
    task = get_task()
    all_pairs = task.get("train", []) + task.get("test", [])
    passed = all(p(pair["input"]) == pair["output"] for pair in 
all_pairs)
    print(f"🧪 {task['metadata']['task_id']} result: {passed}")

if __name__ == "__main__":
    main()
