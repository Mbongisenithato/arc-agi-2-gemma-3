import os

def write_solution(task_id, code, metadata=None):
    """
    Writes a solution script for a given task ID.

    Args:
        task_id (int): The numeric ID of the task (e.g., 1 for 
task001).
        code (str): The Python code to write into the file.
        metadata (dict, optional): Metadata to include as a comment 
header.
    """
    filename = f"task{task_id:03}.py"
    header = ""

    if metadata:
        header_lines = [f"# {key}: {value}" for key, value in 
metadata.items()]
        header = "\n".join(header_lines) + "\n\n"

    with open(filename, "w") as f:
        f.write(header + code)

    print(f"✅ Solution written to {filename}")


