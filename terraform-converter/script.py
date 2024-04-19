import hcl2

def parse_terraform(file_path):
    with open(file_path, 'r') as f:
        terraform_config = hcl2.load(f)

    resources = []
    parse_resources(terraform_config, resources)
    return resources

def parse_resources(config, resources, indent_level=0):
    for block_type, blocks in config.items():
        if block_type == "provider":
            resources.append({
                "type": block_type,
                "name": "provider",
                "indent": indent_level
            })
        else:
            for block_content in blocks:
                if isinstance(block_content, dict):
                    for block_name, block_body in block_content.items():
                        resources.append({
                            "type": block_type,
                            "name": block_name,
                            "indent": indent_level
                        })
                        if isinstance(block_body, dict):
                            parse_resources(block_body, resources, indent_level + 1)
                else:
                    resources.append({
                        "type": block_type,
                        "name": block_content,
                        "indent": indent_level
                    })

# Example usage:
file_path = "C:/Development/D2/terraform-converter/sample-tf/single-ec2.tf"
parsed_resources = parse_terraform(file_path)

for resource in parsed_resources:
    print(" " * (resource["indent"] * 4) + f"{resource['type']} '{resource['name']}'")
