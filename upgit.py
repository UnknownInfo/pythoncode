import subprocess
process = subprocess.Popen(["git", "add","."])
process = subprocess.Popen(["git", "commit","-m", "'Another update'"])
process = subprocess.Popen(["git", "push","-u", "origin", "master"])
process.wait()

print("Upload completed!")
process = subprocess.Popen(["git", "status"])