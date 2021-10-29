from setuptools import setup

with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()

NAME = 'pytimeconv'
VERSION = '0.0.1'

setup(
    name=NAME,
    version=VERSION,
    author='Vardë',
    author_email='ichunjo.le.terrible@gmail.com',
    description='Basic time conversion module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Ichunjo/pytimeconv',
    packages=['pytimeconv'],
    package_data={
        'pytimeconv': ['py.typed'],
    },
    python_requires='>=3.9',
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
