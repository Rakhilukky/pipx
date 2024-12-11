import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: pipx.py [pip commands...]")
        sys.exit(1)
    cmd_args = sys.argv[1:]
    if 'x3' in cmd_args:
        cmd_line = f"python -m pip3 {' '.join(cmd_args)}"
    else:
        cmd_line = f"python -m pip {' '.join(cmd_args)}"
    os.system(cmd_line)

if __name__ == "__main__":
    main()

