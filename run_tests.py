import os
import subprocess

# Directory containing the test modules
test_directory = 'tests'

# List of test modules in the desired execution order
test_modules = [
    'test_warehouse_user.py',
    'test_onprem_user.py',
    'test_settings.py',
    'test_export.py'
]

# Additional command-line options
additional_options = ['-v', '--demo']  # Include verbose mode and the demo option

# Run tests in the specified order
if __name__ == "__main__":
    for test_module in test_modules:
        # Construct the full path to the test module
        module_path = os.path.join(test_directory, test_module)
        
        # Construct the pytest command with test module and additional options
        command = ['pytest'] + additional_options + [module_path]
        
        # Run the pytest command
        subprocess.run(command, check=True)
