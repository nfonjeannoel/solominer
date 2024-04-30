import os

directory = os.path.dirname(os.path.realpath(__file__))
print(f'Running all Python files in the directory: {directory}')


# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.py') and filename != 'runner.py':
        # Construct the full path to the Python file
        filepath = os.path.join(directory, filename)
        # Execute the Python file
        exec(open(filepath).read())
