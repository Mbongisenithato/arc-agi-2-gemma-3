def p(input_grid):
    """
    Inverts a binary grid: 0 → 1 and 1 → 0.
    """
    return [[1 - cell for cell in row] for row in input_grid]

def get_task():
    """
    Returns a sample ARC-style task dictionary.
    """
    return {
        "train": [
            {"input": [[0, 1], [1, 0]], "output": [[1, 0], [0, 1]]}
        ],
        "test": [
            {"input": [[1, 1], [0, 0]], "output": [[0, 0], [1, 1]]}
        ],
        "metadata": {
            "task_id": "task001",
            "description": "Basic grid inversion task for 
demonstration",
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












