import os
import subprocess

def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        executed_command = subprocess.run( command, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)

        list_output = []
        if executed_command.returncode != 0:
            list_output.append(f"Process exited with code {executed_command.returncode}")
        if not executed_command.stdout and not executed_command.stderr:
            list_output.append("No output produced")
        else:
            if executed_command.stdout:
                list_output.append(f"STDOUT: {executed_command.stdout}")
            if executed_command.stderr:
                list_output.append(f"STDERR: {executed_command.stderr}")
        return " ".join(list_output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
