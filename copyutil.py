import os
import shutil

def copy_svg_files(source_dir, target_dir):
    """
    Copy all .svg files from source_dir to target_dir, including from all subdirectories of source_dir.
    
    Parameters:
    - source_dir (str): The directory to search for .svg files.
    - target_dir (str): The directory where .svg files will be copied.
    """
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".svg"):
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_dir, file)
                
                # Ensure the target directory exists
                os.makedirs(target_dir, exist_ok=True)
                
                # Copy the file
                shutil.copy(source_file_path, target_file_path)
                print(f"Copied: {source_file_path} to {target_file_path}")

# Example usage
source_directory = "C://Users//nathan.goddard//Downloads//vmware-stencils-main//vmware-stencils-main//svg"
target_directory = "C://Development//D2//assets//vmware"

copy_svg_files(source_directory, target_directory)

#import os
#
#def delete_svg_files_with_numbers(directory, numbers):
#    """
#    Deletes .svg files in the specified directory that contain any of the specified numbers in their names.
#    
#    Parameters:
#    - directory (str): The directory to search for .svg files.
#    - numbers (list of str or int): Numbers that, if found in the file name, will lead to the file's deletion.
#    """
#    # Ensure the numbers are in string format for comparison
#    numbers = [str(number) for number in numbers]
#    
#    for file in os.listdir(directory):
#        if file.endswith(".svg") and any(number in file for number in numbers):
#            file_path = os.path.join(directory, file)
#            os.remove(file_path)
#            print(f"Deleted: {file_path}")
#
## Example usage
#directory_path = "C://Development//D2//assets//aws"
#numbers_to_check = [16, 32, 48]
#
#delete_svg_files_with_numbers(directory_path, numbers_to_check)
#
#

#import os
#import re
#
#def rename_files(directory):
#    """
#    Rename files in the specified directory by removing an underscore and a number from the end of their filenames,
#    specifically right before the .svg extension.
#
#    Parameters:
#    - directory (str): The directory to search for files to rename.
#    """
#    # This regex targets an underscore followed by one or more digits right before the .svg extension
#    pattern = re.compile(r'(_\d+)(?=\.svg$)', re.IGNORECASE)
#    
#    for filename in os.listdir(directory):
#        if os.path.isfile(os.path.join(directory, filename)):
#            # Apply the regex to each filename
#            new_name = pattern.sub('', filename)
#            if new_name != filename:  # Only rename if changes are made
#                original_path = os.path.join(directory, filename)
#                new_path = os.path.join(directory, new_name)
#                os.rename(original_path, new_path)
#                print(f"Renamed: '{original_path}' to '{new_path}'")
#
## Example usage
#directory_path = "C://Development//D2//assets//aws"
#rename_files(directory_path)
