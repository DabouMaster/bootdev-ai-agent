import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try: 
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
    
        # Tells if the target directory is valid or not with a boolean
        valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
    
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        content_list = []
        for name in os.listdir(target_dir):
            path = os.path.join(target_dir, name)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            content_list.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
        result = "\n".join(content_list)
        return result
    
    except Exception as e:
        return f'Error: {e}'
