import os
import json
from solution_writer import write_solution

def infer_code_from_description(description):
    """Infer solution code based on task description."""
    if "Invert 0s to 1s" in description:
        return (
            "def solve(input_data):\n"
            "    return [[1 if cell == 0 else cell for cell in row] for row in input_data]"
        )
    # Add more inference rules here if needed
    return (
        "def solve(input_data):\n"
        "    # TODO: implement logic\n"
        "    return input_data"
    )

def load_tasks_from_folder(folder):
    """Load tasks from the specified folder and infer code."""
    tasks = {}
    if not os.path.exists(folder):
        print(f"⚠️ Folder '{folder}' does not exist.")
        return tasks

    for filename in os.listdir(folder):
        if filename.startswith("task") and filename.endswith(".json"):
            filepath = os.path.join(folder, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                task_id = data["metadata"]["task_id"]
                description = data["metadata"].get("description", "")
                code = infer_code_from_description(description)
                metadata = data["metadata"]
                tasks[task_id] = {"code": code, "metadata": metadata}
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")
    return tasks

def main():
    folder = "tasks"         # ✅ Changed from 'predictions' to 'tasks'
    output_dir = "solutions"
    os.makedirs(output_dir, exist_ok=True)

    tasks = load_tasks_from_folder(folder)

    for task_id, details in tasks.items():
        write_solution(
            task_id,
            details["code"],
            details.get("metadata", {}),
            output_dir=output_dir
        )

    print(f"\n🧾 {len(tasks)} tasks written to '{output_dir}/'")

if __name__ == "__main__":
    main()