import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try: 
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10_000
    
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} charachters]'
        return file_content_string

    except Exception as e:
        return f'Error: {e}'

