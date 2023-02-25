from setuptools import setup, find_packages

test_requirements = [
    "mock",
    "pytest",
    "mockito",
    "moto",
    "pytest-cov",
    "pytest-sugar",
    "requests_mock",
    "behave",
    "pyHamcrest",
    "boto3_mocking",
]


setup(
    name="puzzle-utils",
    version="0.1.0",
    packages=find_packages(where="src/main/python"),
    package_dir={
        "puzzle_utils": "src/main/python/puzzle_utils",
    },
    install_requires=["requests", "timecode", "dataclasses", "jmespath", "boto3"],
    tests_require=test_requirements,
    extras_require={"test": test_requirements},
)
