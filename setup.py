from setuptools import setup

setup(
    name="threads-cli",
    version="1.1.2",
    packages=["threads_cli"],
    install_requires=["requests", "typer", "rich", "python-dotenv"],
    entry_points={"console_scripts": ["threads-cli=threads_cli.cli:main"]}
)
