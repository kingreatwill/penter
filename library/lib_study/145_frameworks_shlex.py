import shlex
# 3.8 print(shlex.join(['echo', '-n', 'Multiple words']))
import shlex, subprocess

subprocess.Popen(shlex.split('ls -l /'))

