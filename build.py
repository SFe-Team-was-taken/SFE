import shutil
import subprocess

files = ["code-of-conduct", "LICENSE", "contributing", "SECURITY", "draft-revision-history"]

for file in files:
    shutil.copy(file+".md", "docs/"+file+".md")
subprocess.run(["zensical", "build", "--clean"])