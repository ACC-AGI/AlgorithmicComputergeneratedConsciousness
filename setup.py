from setuptools import setup, find_packages

setup(
    name="ACC",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["gradio_client"],
    author="Tej Andrews",
    description="Tej's Consciousness Model - A persistent AI chat session with Z3ta",
    url="https://github.com/ACC-AGI/ACC",  # Change to your actual GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
