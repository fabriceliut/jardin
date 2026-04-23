import os
import subprocess

# Root directory
root_dir = "/Users/fabriceliut/Documents/GitHub/jardin/_notes"

# Get all .md files in _notes recursively
all_files = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            all_files.append(os.path.abspath(os.path.join(root, file)))

# Get modified files from git status (only those in _notes)
# Use -c core.quotepath=false to get UTF-8 paths
git_status = subprocess.check_output(["git", "-c", "core.quotepath=false", "status", "--porcelain", root_dir]).decode("utf-8")
modified_files = []
for line in git_status.split("\n"):
    if line.strip() == "": continue
    path = line[3:].strip().strip('"')
    full_path = os.path.abspath(os.path.join("/Users/fabriceliut/Documents/GitHub/jardin", path))
    if full_path.startswith(root_dir):
        modified_files.append(full_path)

# Normalize paths for comparison
all_files_set = set(all_files)
modified_files_set = set(modified_files)

# Files that are NOT modified in git status
unmodified_files = all_files_set - modified_files_set

# Also exclude files committed in the last 200 commits
git_log_files = subprocess.check_output(["git", "-c", "core.quotepath=false", "log", "-n", "200", "--name-only", "--pretty=format:", root_dir]).decode("utf-8")
committed_files = set()
for line in git_log_files.split("\n"):
    line = line.strip().strip('"')
    if line.endswith(".md"):
        full_path = os.path.abspath(os.path.join("/Users/fabriceliut/Documents/GitHub/jardin", line))
        if full_path.startswith(root_dir):
            committed_files.add(full_path)

remaining_files = sorted(list(unmodified_files - committed_files))

print(f"Total files in _notes: {len(all_files)}")
print(f"Currently modified in _notes: {len(modified_files)}")
print(f"Recently committed in _notes: {len(committed_files)}")
print(f"Remaining to process: {len(remaining_files)}")

for f in remaining_files:
    print(f)
