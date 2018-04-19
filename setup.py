"""pylttb - downsampling of given series using Largest Triangle Three Buckets method."""

from setuptools import setup, find_packages

with open('README.rst') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='pylttb',
    license='MIT',
    description=__doc__,
    use_scm_version=True,
    long_description=LONG_DESCRIPTION,
    platforms=["Linux", "Unix"],
    setup_requires=['setuptools_scm'],
    install_requires=['numpy'],
    tests_require=['numpy'],
    author='Konrad Jałowiecki <dexter2206@gmail.com>',
    author_email='dexter2206@gmail.com',
    packages=find_packages(),
    keywords='downsampling largest triangl three buckest'
)
