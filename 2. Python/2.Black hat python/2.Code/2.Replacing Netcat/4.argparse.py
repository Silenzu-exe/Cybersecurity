import argparse

parser = argparse.ArgumentParser(description="Simple netcat-style tool")
parser.add_argument("-t", "--target", default="127.0.0.1", help = "target IP")
parser.add_argument("-p", "--port", type = int, default=9999, help = "target port")
parser.add_argument("-l", "--listen", action = "store_true", help = "listen mode")
parser.add_argument("-e", "--execute", help = "command to execute on connection")
parser.add_argument("-u", "--upload", help = "filename to save uploaded data as")

args = parser.parse_args()



'''   how to use argparse with 1.netcat.py
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Run a shell command")
parser.add_argument("-e", "--execute", help="command to execute")
args = parser.parse_args()

if args.execute:
    output = subprocess.check_output(args.execute, shell=True, stderr=subprocess.STDOUT)
    print(output.decode())

'''