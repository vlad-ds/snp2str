from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='snp2str',
      version='0.1',
      description='TODO',
      url='http://github.com/TODO', # TODO add public git url
      author='Vlad Gheorghe',
      author_email='vlad.datapro@gmail.com',
      license='TODO',
      packages=['snp2str'],
      scripts=['bin/snp2str'],
      install_requires=required,
      include_package_data=True,
      zip_safe=False)
