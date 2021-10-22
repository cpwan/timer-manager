import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timer manager",
    version="0.0.1",
    author="Ching Pui WAN",
    author_email="cpwan@ust.hk",
    description="A small timer package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cpwan/timer-manager",
    project_urls={
        "Bug Tracker": "https://github.com/cpwan/timer-manager/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)