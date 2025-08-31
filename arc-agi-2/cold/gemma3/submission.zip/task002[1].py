def solve(input_grid):
    """
    Increments each cell value in the grid by 1.
    This is the core function used by the evaluator.
    """
    return [[cell + 1 for cell in row] for row in input_grid]

def get_task():
    """
    Returns the full ARC-style task dictionary.
    Useful for training, metadata, and standalone testing.
    """
    return {
        "train": [
            {"input": [[2, 2], [2, 2]], "output": [[3, 3], [3, 3]]}
        ],
        "test": [
            {"input": [[1, 3], [0, 2]], "output": [[2, 4], [1, 3]]}
        ],
        "metadata": {
            "task_id": "task002",
            "description": "Increment each cell in the grid by 1",
            "source": "Gemma3 ARC-style framework",
            "difficulty": "easy"
        }
    }

def main():
    """
    Runs local evaluation using solve() on all train/test pairs.
    """
    task = get_task()
    all_pairs = task.get("train", []) + task.get("test", [])
    passed = all(solve(pair["input"]) == pair["output"] for pair in all_pairs)
    print(f"🧪 {task['metadata']['task_id']} result: {passed}")

if __name__ == "__main__":
    main()