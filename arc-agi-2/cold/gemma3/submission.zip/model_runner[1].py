from evaluator import evaluate

task_ids = ["task001", "task002", "task003"]

def run_all_tasks():
    for task_id in task_ids:
        try:
            result = evaluate(task_id)
            print(f"{task_id}: {'✅ Passed' if result else '❌ Failed'}")
        except Exception as e:
            print(f"❌ Error in {task_id}: {e}")

if __name__ == "__main__":
    run_all_tasks()