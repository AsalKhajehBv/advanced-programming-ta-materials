from setuptools import setup, find_packages

setup(
    name="math_tools",          # Name of the package
    version="0.0.1",            # Version number
    description="Small math helpers",  # Short description
    packages=find_packages(),   # Automatically finds all packages in folder
                                # and returns a list of their names
                                # to include when installing your library
    python_requires=">=3.8",    # Python version requirement
)
