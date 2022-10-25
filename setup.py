from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

# TODO add requirements

setup(name='snp2str',
      version='0.1',
      description='TODO',
      url='http://github.com/TODO',
      author='Vlad Gheorghe',
      author_email='vlad.datapro@gmail.com',
      license='TODO',
      packages=['snp2str'],
      scripts=['bin/snp2str'],
      include_package_data=True,
      zip_safe=False)
