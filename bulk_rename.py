import os #provides a way to interact with the operating system
directory = '/Users/arshpreetmultani/Desktop/comp10125'# Folder containing files to rename
pattern = 'Prgm_'  # Prefix for renamed files
file_extension = '.py'  # Target file type (change as needed)
def bulk_rename_files(directory, pattern, file_extension): #directory, pattern, file_extension are placeholders, they temporarily hold values passed into the function
    try:
        # List all files in the directory
        files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
        
        # Loop through and rename each file
        for index, file in enumerate(files, start=1):
            old_path = os.path.join(directory, file)
            new_filename = f"{pattern}{index}{file_extension}"
            new_path = os.path.join(directory, new_filename)
            
            os.rename(old_path, new_path)
            print(f"Renamed: {file} → {new_filename}")
    
    except FileNotFoundError:
        print("Directory not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
bulk_rename_files(directory, pattern, file_extension)