from setuptools import setup, find_packages

setup(
    name="DeepThought Artificial Intelligence (AI) Engine powered by AI",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "openai>=0.27.0"
    ],
    author="Ward Bekker",
    author_email="ward@wardbekker.com",
    description="A Python library for AI-based conditional logic using OpenAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/wardbekker/deepthought_ai_framework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)