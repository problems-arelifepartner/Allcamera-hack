import os

def create_directories():
    # Define the directories to be created
    directories = ["dir1", "dir2"]

    for directory in directories:
        try:
            # Create the directory
            os.makedirs(directory, exist_ok=True)
            print(f"Directory '{directory}' created successfully.")
            
            # Create the VBScript content
            vbs_code = '''do
MsgBox "Hay guys"
loop'''
            
            # Define the file path for the VBScript
            vbs_filename = os.path.join(directory, "message.vbs")
            
            # Write the VBScript to the file
            with open(vbs_filename, 'w') as vbs_file:
                vbs_file.write(vbs_code)
            print(f"VBScript file 'message.vbs' created in '{directory}'.")
        
        except Exception as e:
            print(f"Error creating directory or VBScript in '{directory}': {e}")

if __name__ == "__main__":
    create_directories()
