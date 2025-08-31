def solve(input_grid):
    """
    Doubles each cell value in the grid.
    This is the core function used by the evaluator.
    """
    return [[cell * 2 for cell in row] for row in input_grid]

def get_task():
    """
    Returns a sample ARC-style task dictionary.
    """
    return {
        "train": [
            {"input": [[1, 2], [3, 4]], "output": [[2, 4], [6, 8]]}
        ],
        "test": [
            {"input": [[0, 0], [0, 0]], "output": [[0, 0], [0, 0]]}
        ],
        "metadata": {
            "task_id": "task003",
            "description": "Double each cell value in the grid",
            "source": "Gemma3 ARC-style framework",
            "difficulty": "easy"
        }
    }

def main():
    """
    Runs evaluation on train and test samples using solve().
    """
    task = get_task()
    all_pairs = task.get("train", []) + task.get("test", [])
    passed = all(solve(pair["input"]) == pair["output"] for pair in all_pairs)
    print(f"🧪 {task['metadata']['task_id']} result: {passed}")

if __name__ == "__main__":
    main()