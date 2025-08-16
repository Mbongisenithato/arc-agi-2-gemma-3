import zipfile

with zipfile.ZipFile("submission.zip", "w") as zipf:
    zipf.write("solution.py")
    zipf.write("predict.py")
