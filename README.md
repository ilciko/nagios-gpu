# Nagios gpu plugin for Talos

The following package implement an interface with ELK stack and Ansible adding an ML framework. Documentation:
[TALOS-ML](https://share.e4company.com/display/OT/ML)
The package is required by Talos service (AIOPS platform).


# BUILD and UPLOAD
python3 -m build
twine upload --config-file .pypirc --repository nexus dist/*
