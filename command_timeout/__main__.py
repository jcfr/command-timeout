import sys
import subprocess

def main():
    subprocess.run(sys.argv[2:],
        stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr,
        timeout=int(sys.argv[1]))
