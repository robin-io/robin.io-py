from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='robin.io-py',
    version='0.0.3',
    description='Robin.io-py is a Python SDK built to communicate with the Robinapp API. Now you can integrate Robin.io with minimal effort and quickly setup a real-time messaging platform in your Web application.',
    url='https://github.com/robin-io/robin.io-py/',

    author='Samuel Olufeko',
    author_email='samuel@acumen.digital',

    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],

    install_requires=['requests','websocket-client'],

    license='MIT',

    keywords='notifications python library',

    packages=['robin'],
    zip_safe=False
)