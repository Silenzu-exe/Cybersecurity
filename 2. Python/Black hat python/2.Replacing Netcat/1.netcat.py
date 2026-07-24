import subprocess

output = subprocess.check_output("ls ~", shell = True, stderr = subprocess.STDOUT)
print(output.decode())