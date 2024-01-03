from setuptools import setup, find_packages

setup(
    name="FinPyTrader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "finpytrader = FinPyTrader.FinPyTrader:main",
        ],
    },
    author="Khaireddine Arbouch",
    author_email="khaireddine.arbouch@bahcesehir.edu.tr",
    description="A Python package for algorithmic trading",
    license="MIT",
    keywords="algorithmic trading finance",
    url="https://github.com/khaireddine-tech/FinPyTrader",
)