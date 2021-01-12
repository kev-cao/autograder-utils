import sys, os, re

def get_test_methods(f):
    """
    Fetches all of the methods annotated with @Test in the given file.

    Params:
    f: The file object of the test file.

    Return:
    [str]: List of @Test-annotated methods by name.
    """
    file_str = f.read()
    method_pattern = r'@Test[\r\n\t ]*.+ (\w+)\(.*\)'
    return re.findall(method_pattern, file_str)

def create_compile_command(file_name):
    """
    Creates the bash command for compiling a JUnit test.

    Params:
    file_name (str): The file name of the test to compile.

    Return:
    str: The bash command for compiling.
    """
    return f"javac -d classes -cp classes/:junit-jupiter-api-5.7.0.jar:apiguardian-api-1.1.1.jar {file_name}"

def create_run_command(class_name, method_name):
    """
    Creates the bash command for running a JUnit test.

    Params:
    class_name (str): The class name of the test to run.
    method_name (str): The name of the method of the class to run.

    Return:
    str: The bash command for running.
    """
    return f"java -jar junit-platform-console-standalone-1.7.0.jar --fail-if-no-tests --disable-banner --details-theme=ascii --disable-ansi-colors -cp classes --select-method={class_name}#{method_name}"

def process_file(f):
    file_name = os.path.basename(f.name)
    print(f"--------------------------\nProcessing {file_name}\n--------------------------")
    print(f"Compile: {create_compile_command(file_name)}\n")

    class_name = file_name[:file_name.index('.java')]
    methods = get_test_methods(f)

    for method in methods:
        print(f"Method: {method}")
        print(f"\tRun: {create_run_command(class_name, method)}\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You must provide either the directory containing the files or the file itself.")
    else:
        # Process each of the arguments.
        for arg in sys.argv[1:]:
            try:
                # Check if the given argument is a directory first.
                # If so, process all .java files in the directory.
                for file_name in os.listdir(arg):
                    if file_name.endswith('.java'):
                        with open(f'{arg}/{file_name}', 'r') as f:
                            process_file(f)
            except (FileNotFoundError, NotADirectoryError):
                # Check if the given argument is a file.
                try:
                    with open(arg, 'r') as f:
                        if arg.endswith('.java'): # Process only .java files.
                            process_file(f)
                except FileNotFoundError:
                    print(f"No directory or file '{arg}' exists.")
