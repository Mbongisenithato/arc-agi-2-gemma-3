def write_solution(task_id, code):
    with open(f"task{task_id:03}.py", "w") as f:
        f.write(code)
