# Copyright 2020, E4 Computer Engineering SpA.
#
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
        name='nagios-gpu-plugin',
        version='0.1.0',
        author='Marco Cicala',
        author_email='marco.cicala@e4company.com',
        description="Nagios GPU Plugin",
        long_description=long_description,
        long_description_content_type="text/markdown",
        license="MIT",
        keywords="nagios nvidia smi gpu plugin",
        url='https://github.com/ilciko/nagios-nvidia-smi-plugin',
        namespace_packages=['nagios-gpu'],
        provides=['nagios-gpu'],
        install_requires=["argparse","nagiosplugin"],
        scripts=["check_nvidiasmi.py"]
)
