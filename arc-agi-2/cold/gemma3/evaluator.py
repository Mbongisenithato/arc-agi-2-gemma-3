import json
import importlib
import sys

def load_task(path):
    """
    Load a task JSON file from the given path.
    """
    with open(path) as f:
        return json.load(f)

def evaluate(p, task):
    """
    Evaluate a function `p` against all input-output pairs in task.

    Args:
        p (function): The solution function to test.
        task (dict): The task dictionary containing train/test/
arc-gen pairs.

    Returns:
        bool: True if all outputs match, False otherwise.
    """
    all_pairs = task.get("train", []) + task.get("test", []) + task.
get("arc-gen", [])
    return all(p(pair["input"]) == pair["output"] for pair in 
all_pairs)

def main(task_id):
    """
    Dynamically import and evaluate a task module by ID.
    """
    try:
        task_module = importlib.import_module(task_id)
        p = getattr(task_module, "p")
        get_task = getattr(task_module, "get_task")
    except (ImportError, AttributeError) as e:
        print(f"❌ Failed to load task module '{task_id}': {e}")
        sys.exit(1)

    task = get_task()
    print(f"✅ Loaded task: {task['metadata']['task_id']}")
    result = evaluate(p, task)
    print(f"🧪 Evaluation result: {result}")

if __name__ == "__main__":
    task_id = "task001"  # You can make this dynamic later
    main(task_id)
