"""A small local command runner, not a shell or a sandbox."""
import os
import shlex
import subprocess

def parse_command(text):
    """Preserve quoted arguments on POSIX; use native parsing on Windows."""
    if not text.strip():
        raise ValueError("Enter a command")
    return text if os.name == "nt" else shlex.split(text)

def run_command(text):
    return subprocess.run(parse_command(text), shell=False, check=False).returncode

def main():
    while True:
        try:
            command = input("> ")
            if command.strip().lower() == "exit":
                break
            if not command.strip():
                continue
            code = run_command(command)
            if code:
                print(f"Command exited with status {code}")
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nInterrupted")
        except (OSError, ValueError) as error:
            print(f"Error: {error}")
    print("good bye")

if __name__ == "__main__":
    main()
