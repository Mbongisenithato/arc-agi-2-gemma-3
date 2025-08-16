import json

def load_task(path):
    with open(path) as f: return json.load(f)

def evaluate(p, task):
    for pair in task["train"] + task["test"] + task["arc-gen"]:
        if p(pair["input"]) != pair["output"]: return False
    return True

if __name__ == "__main__":
    from task001 import p
    task = load_task("task001.json")
    print("Evaluation result:", evaluate(p, task))
