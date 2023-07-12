import os
import re

# Define the directory path where your files are located
directory_path = '.'

# Define the regular expression pattern to match the iframe tags
pattern = r'<iframe width="560" height="315" src="https:\/\/www\.youtube\.com\/embed\/([\w-]+)" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen><\/iframe>'

# Define the replacement string with the Hugo shortcode format
replacement = r'{{< youtube id="\1" autoplay="true" >}}'

# Iterate over the files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Read the contents of the file with explicit encoding specification
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # Use re.sub() to replace the iframe tags with the Hugo shortcodes
    updated_content = re.sub(pattern, replacement, file_content)
    
    # Write the updated contents back to the file with explicit encoding specification
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
