import shlex
import subprocess

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return ""
    try:
        output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output.decode(errors="replace")

print(execute('ls -la'))