import subprocess

def run_script(script_name, interactive=False):
    try:
        print(f"Executing {script_name}...")
        
        if interactive:
            # Run interactively without capturing output (for scripts that need user input)
            subprocess.run(["python", script_name], check=True)
        else:
            # Run with captured output (for non-interactive scripts)
            result = subprocess.run(["python", script_name], check=True, text=True, capture_output=True)
            print(f"Output from {script_name}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_name}: {e.stderr}")
        exit(1)

if __name__ == "__main__":
    # Step 1: Execute open.py (interactive mode)
    run_script("open.py", interactive=True)
    
    # Step 2: Execute video.py
    run_script("video.py")
    
    # Step 3: Execute integrate.py
    run_script("integrate.py")

    run_script("permission.py")
    
    # Step 4: Execute save.py
    run_script("save.py")

    print("All scripts executed successfully.")
