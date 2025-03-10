from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="og_query_runner",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    author="Mohammad Choupan",
    author_email="mohamad.choupan@opencomply.io",
    description="A package to run queries and save results on a given opencomply instance.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/opengovern/og_query_runner",
    license=open("LICENSE").read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)


