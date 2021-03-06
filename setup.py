import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="azsc",
    version="0.1.1",
    author="Davide Mauri",
    author_email="info@davidemauri.it",
    description="A script language created from AZ CLI commands to make deployment and management of Azure resources as simple and intelligent as possibile.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yorek/azure-script",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Utilities"
    ],
    py_modules=['azsc'],
    install_requires=[
        'Click',
        'lark-parser==0.6.4',
        'setuptools'        
    ],
    entry_points={
        'console_scripts': [
            'azsc=azsc.azsc:cli'
        ]
    }        
)