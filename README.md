
# Cloud Architecture Diagrams with D2

This repository contains assets and classes for creating cloud architecture diagrams using [D2](https://d2lang.com), for services including AWS, Azure, GCP, and VMware Cloud.

## Structure

- `assets/`: This directory contains image icons for the various cloud services.
- `workspace/`: Here you'll find class directories for each cloud service. These can be imported into your diagrams with the import method.

## Usage

To use the predefined nodes for each cloud service, you can import them into your D2 files as follows:

```plaintext
...@../aws-nodes
...@../azure-nodes
```

Below is a simple example of how to use D2 to create a diagram featuring AWS services:

```plaintext
...@../aws-nodes
...@../general-nodes

VPC.class: Virtual-private-cloud-VPC
VPC: {
    near:top-left 
    label: VPC AZ-1
    Server1.class: Arch_Amazon-EC2

    Server1: {
        tooltip: Apache2 & PHP
        label: Webserver
    }
    Server2.class: Arch_Amazon-RDS

    Server1 <-> Server2: DB Connection
}

VPC2.class: Virtual-private-cloud-VPC
VPC2: {
    near:top-right
    label: VPC AZ-2
    Server1.class: Arch_Amazon-EC2
    Server2.class: Arch_Amazon-RDS
    # Connections 
    Server1 <-> Server2: DB Connection
}

VPC.Server2 -> VPC2.Server2: Read Replication
```

Replace `...@../aws-nodes` with the path relative to your D2 file where the AWS node definitions are stored. The same applies for `...@../general-nodes` and other services.

## Contributing

Contributions are welcome! If you have any suggestions or additions, feel free to open an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE](LICENSE.md) file for details.
