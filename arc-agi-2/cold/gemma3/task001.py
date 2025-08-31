def solve(input_grid):
    """
    Inverts 0s to 1s, leaves all other values unchanged.
    This is the core function used by the evaluator.
    """
    return [[1 if cell == 0 else cell for cell in row] for row in input_grid]


def get_task():
    """
    Returns the full ARC-style task dictionary.
    Useful for training, metadata, and standalone testing.
    """
    return {
        "train": [
            {"input": [[0, 1], [1, 0]], "output": [[1, 1], [1, 1]]},
            {"input": [[0, 2], [3, 0]], "output": [[1, 2], [3, 1]]}
        ],
        "test": [
            {"input": [[1, 1], [0, 0]], "output": [[1, 1], [1, 1]]}
        ],
        "metadata": {
            "task_id": "task001",
            "description": "Invert 0s to 1s, leave others unchanged",
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
