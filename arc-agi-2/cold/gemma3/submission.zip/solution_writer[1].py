import os

def write_solution(task_id, code, metadata=None, output_dir="."):
    """
    Writes a solution script for a given task ID.

    Args:
        task_id (str): The full task ID string (e.g., "task001").
        code (str): The Python code to write into the file.
        metadata (dict, optional): Metadata to include as a comment header.
        output_dir (str): Directory to save the solution file.
    """
    filename = f"{task_id}.py"  # ✅ Fixed: no extra 'task' prefix
    filepath = os.path.join(output_dir, filename)
    header = ""

    if metadata:
        header_lines = [f"# {key}: {value}" for key, value in metadata.items()]
        header = "\n".join(header_lines) + "\n\n"

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(header + code)
        print(f"✅ Solution written to {filepath}")
    except Exception as e:
        print(f"❌ Failed to write solution: {e}")

def example_code():
    return (
        "def solve(input_data):\n"
        "    # TODO: implement solution\n"
        "    return input_data"
    )

if __name__ == "__main__":
    # Example usage
    task_id = "task001"  # ✅ Use full string ID
    code = example_code()
    metadata = {
        "Author": "Mbongiseni Thato",
        "Task": "ARC Task 001",
        "Description": "Initial solution template"
    }
    write_solution(task_id, code, metadata, output_dir="solutions")