# evaluator_batch.py

import os
import json
import importlib.util

def evaluate(task_id, base_dir="gemma3"):
    task_path = os.path.join(base_dir, f"{task_id}.json")
    solution_path = os.path.join(base_dir, f"{task_id}.py")

    try:
        # Load task data
        with open(task_path, "r") as f:
            task_data = json.load(f)

        # Dynamically import the solution module
        spec = importlib.util.spec_from_file_location("solution", solution_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Evaluate all train and test samples
        all_pairs = task_data.get("train", []) + task_data.get("test", [])
        for i, pair in enumerate(all_pairs):
            predicted = module.solve(pair["input"])
            if predicted != pair["output"]:
                print(f"{task_id}: ❌ Failed on sample {i}")
                print("Input:    ", pair["input"])
                print("Expected: ", pair["output"])
                print("Predicted:", predicted)
                return False

        return True
    except Exception as e:
        print(f"{task_id}: ⚠️ Error during evaluation → {e}")
        return False

# Batch evaluation
for task_id in ["task001", "task002", "task003"]:
    result = evaluate(task_id)
    print(f"{task_id}: {'✅ Passed' if result else '❌ Failed'}")