import importlib
from evaluator import evaluate, load_task

task_modules = ["task001", "task002", "task003"]

def run_all_tasks():
    for module_name in task_modules:
        try:
            module = importlib.import_module(module_name)
            p = getattr(module, "p")
            get_task = getattr(module, "get_task")
            task = get_task()
            print(f"✅ Loaded {module_name}: {task['metadata']['task_id']}")
            result = evaluate(p, task)
            print(f"🧪 {module_name} result: {result}")
        except Exception as e:
            print(f"❌ Error in {module_name}: {e}")

if __name__ == "__main__":
    run_all_tasks()
