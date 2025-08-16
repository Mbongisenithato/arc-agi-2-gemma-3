import importlib

# List of task modules
task_modules = ["task001", "task002", "task003"]

def run_all_tasks():
    for module_name in task_modules:
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, "main"):
                print(f"Running {module_name}.main()")
                module.main()
            else:
                print(f"{module_name} has no main() function.")
        except Exception as e:
            print(f"Error in {module_name}: {e}")

if __name__ == "__main__":
    run_all_tasks()
