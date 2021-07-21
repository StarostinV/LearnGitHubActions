from setuptools import setup, find_packages


classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

setup(
    name='learn_actions',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    version='1.0.0',
    author='Vladimir Starostin',
    author_email='vladimir.starostin@uni-tuebingen.de',
    url='https://github.com/StarostinV/LearnGitHubActions',
    license='MIT',
    python_requires='>=3.6',
    classifiers=classifiers,
)
