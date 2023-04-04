from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    "Programming Language :: Python :: 3"
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent'
]

# with open("README.md", "r") as fh:
#     long_description = fh.read()

description = "Tool Container"

setup(
    name='toolcontainer',
    version='0.1',
    packages=find_packages(),
    # TODO: fix
    package_data= {
        "toolcontainer": ['*', '*/*', '*/*/*', '*/*/*/*'],
    },
    url='',
    project_urls={
        'Source': '',
        'Tracker': '',
    },
    author='ShadowCodeCz',
    author_email='shadow.code.cz@gmail.com',
    description=description,
    long_description="",
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    keywords='mini tunner',
    install_requires=["alphabetic_timestamp", "pandas"],
    entry_points={
        'console_scripts': [
            'tool-container=toolcontainer:main',
            'toco=toolcontainer:main',
        ]
    }
)