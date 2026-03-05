import subprocess

while True :
    try:
        command = input("> ")
        if command.lower() == "exit":
            break
        subprocess.run(command)
    except Exception :
        continue
        
print("good bye")