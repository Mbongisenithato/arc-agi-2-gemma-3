def p(input_grid):
    """
    Transformation: double each cell value.
    """
    return [[cell * 2 for cell in row] for row in input_grid]

def get_task():
    """
    Returns a sample ARC-style task dictionary.
    """
    return {
        "train": [
            {"input": [[2, 2], [2, 2]], "output": [[4, 4], [4, 4]]}
        ],
        "test": [
            {"input": [[1, 3], [0, 2]], "output": [[2, 6], [0, 4]]}
        ],
        "metadata": {
            "task_id": "task002",
            "description": "Simple grid doubling task",
            "source": "Gemma3 ARC-style framework",
            "difficulty": "easy"
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
