from setuptools import setup, find_packages


def long_description():
    with open("README.md") as readme:
        return readme.read()


setup(
    name="woot",
    version="0.0.1",
    author="Aleksei Ushakov",
    author_email="isfluid@proton.me",
    description="Still simple Chatwoot API wrapper",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="Cooperative Non-Violent Public License v7 or later (CNPLv7+)",
    project_urls={
        "Bug Tracker": "https://github.com/dearkafka/woot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "httpx>=0.23.0",
        "python-slugify",
        "httpx",
        "python-status",
        "pydantic==1.10.13",
    ],
)
