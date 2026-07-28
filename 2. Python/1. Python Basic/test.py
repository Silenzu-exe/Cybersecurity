import argparse
import subprocess

parser = argparse.ArgumentParser(description="Run a shell command")
parser.add_argument("-e", "--execute", help="command to execute")
args = parser.parse_args()

if args.execute:
    output = subprocess.check_output(args.execute, shell=True, stderr=subprocess.STDOUT)
    print(output.decode())