from functions.get_file_content import get_file_content

file_content = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(file_content)}")
print(f"lorem.txt truncated: {'truncated' in file_content}")

file_content = get_file_content("calculator", "main.py")
print(file_content)

file_content = get_file_content("calculator", "pkg/calculator.py")
print(file_content)

file_content = get_file_content("calculator", "/bin/cat")
print(file_content)

file_content = get_file_content("calculator", "pkg/does_not_exist.py")
print(file_content)
