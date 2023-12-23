import os

def print_tree(directory, indent=''):
    files = os.listdir(directory)
    files.sort()  # Sort files alphabetically

    for file in files:
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            # Print file name with proper indentation
            print(f"{indent}|-- {file}")
        elif os.path.isdir(path):
            # Print directory name with proper indentation
            print(f"{indent}|-- {file}/")
            print_tree(path, indent + "|   ")

# Example usage
directory_path = r"C:\Users\kinla\Documents\All_github_repo\gites\gites"  # Replace with your desired directory path
print_tree(directory_path)