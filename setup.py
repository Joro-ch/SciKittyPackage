from setuptools import setup

readme = open("./READEME.md", "r")

setup(
    name='scikitty',
    packages=['scikitty'],
    version=0.1,
    description='A package to create Decision Trees like Scikitlearn.',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='John Rojas',
    author_email='john.rojas.chinchilla@gmail.com',
    url='https://github.com/JohnRojas222/SciKittyPackage/',
    download_url='https://github.com/JohnRojas222/SciKittyPackage/tarball/0.1',
    keywords=['scikitlearn', 'decision trees', 'metrics'],
    classifiers=[],
    license='MIT',
    include_package_data=True
)