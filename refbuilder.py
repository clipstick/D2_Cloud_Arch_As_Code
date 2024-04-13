import os

def generate_code_blocks_to_file(directory, output_file):
    """
    Generate code blocks for each .svg file in the specified directory and write them to an output file.

    Parameters:
    - directory (str): The directory to search for .svg files.
    - output_file (str): The path to the file where the output will be written.
    """
    with open(output_file, 'w') as file:
        for filename in os.listdir(directory):
            if filename.endswith('.svg'):
                # Constructing the full path of the SVG file
                full_path = os.path.abspath(os.path.join(directory, filename))
                name_without_extension = os.path.splitext(filename)[0]
                code_block = f"""{name_without_extension} {{
    icon:{full_path}
    shape:image
    height:50
    style{{
        font:mono
        font-size:14
    }}
}}
"""
                file.write(code_block + "\n")

# Example usage
directory_path = "C://Development//D2//assets//general"
output_file_path = "C://Development//D2//code_blocks_general.txt"
generate_code_blocks_to_file(directory_path, output_file_path)
