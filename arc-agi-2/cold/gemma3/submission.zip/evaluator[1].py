import json
import importlib.util
import os

def load_task(task_id, base_dir="gemma3"):
    """Load task JSON data given a task ID and base directory."""
    task_path = os.path.join(base_dir, f"{task_id}.json")
    with open(task_path, "r") as f:
        return json.load(f)

def evaluate(task_id, base_dir="gemma3"):
    """Evaluate a task by running its solution against all samples."""
    task_data = load_task(task_id, base_dir)
    solution_path = os.path.join(base_dir, f"{task_id}.py")

    try:
        # Dynamically import the solution module
        spec = importlib.util.spec_from_file_location("solution", solution_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Evaluate all train and test samples
        all_pairs = task_data.get("train", []) + task_data.get("test", [])
        for i, pair in enumerate(all_pairs):
            predicted = module.solve(pair["input"])
            expected = pair["output"]
            if predicted != expected:
                print(f"{task_id}: ❌ Failed on sample {i}")
                print("Input:    ", pair["input"])
                print("Expected: ", expected)
                print("Predicted:", predicted)
                return False  # Fail fast on first mismatch

        return True  # All samples passed

    except Exception as e:
        print(f"{task_id}: ⚠️ Error → {e}")
        return False

# Run single task
if __name__ == "__main__":
    task_id = "task001"  # Change this to evaluate other tasks
    result = evaluate(task_id)
    print(f"{task_id}: {'✅ Passed' if result else '❌ Failed'}")