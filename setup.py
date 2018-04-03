import setuptools

setuptools.setup(
    name="apistar_palyground",
    version="0.1.0",
    url="https://github.com/chenl/apistar_palyground",

    author="Chen Rotem Levy",
    author_email="chen@rotemlevy.name",

    description="A RESTful API created to paly with apistar",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
    ],
)
