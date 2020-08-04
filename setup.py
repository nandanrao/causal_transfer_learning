from setuptools import setup, find_packages

setup(
    name='causal_transfer_learning',
    version='0.0.1',
    url='https://github.com/nandanrao/causal_transfer_learning',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn',
        'PICOS',
        'matplotlib',
        'cvxopt',
        'autograd'
    ]
)
