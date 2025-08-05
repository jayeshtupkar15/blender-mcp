import sys
from blender_mcp.server import main as server_main

def main():
    # Extract additional arguments passed after '--'
    if '--' in sys.argv:
        extra_args = sys.argv[sys.argv.index('--') + 1:]
    else:
        extra_args = []

    # Look for --prompt argument
    prompt = None
    if '--prompt' in extra_args:
        idx = extra_args.index('--prompt')
        if idx + 1 < len(extra_args):
            prompt = extra_args[idx + 1]

    # Call the server logic (or replace with your new logic)
    server_main(prompt=prompt)

if __name__ == "__main__":
    main()
