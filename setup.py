from setuptools import setup

setup(
    name="akynovia-ai",
    version="0.1",
    author="Seu Nome",
    author_email="seu-email@example.com",
    description="Assistente virtual Akynovia AI",
    packages=["akynovia_ai"],
    install_requires=[
        "configparser",
        "w3m",
    ],
    entry_points={
        "console_scripts": [
            "akynovia-ai=akynovia_ai.main:main",
        ]
    },
)
