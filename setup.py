from setuptools import setup, find_packages
setup(
    name="GenCBar",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    #scripts=['say_hello.py'],
    install_requires=['pillow>=5.4.1'],
    # metadata to display on PyPI
    author="n79s",
    author_email="",
    description="カスバー画像生成",
    license="MIT",
    keywords="barcode",
    url="https://github.com/n79s/gencbar",
)