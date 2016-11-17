from distutils.core import setup
setup(
  name = 'palmettopy',
  packages = ['palmettopy'], # this must be the same as the name above
  version = '0.1',
  description = 'Palmetto Python Bindings',
  author = 'Ivan Ermilov',
  author_email = 'ivan.s.ermilov@gmail.com',
  url = 'https://github.com/earthquakesan/palmetto-py', # use the URL to the github repo
  download_url = 'https://github.com/earthquakesan/palmetto-py/tarball/0.1', # I'll explain this in a second
  keywords = ['aksw', 'nlp', 'semantic-web'], # arbitrary keywords
  classifiers = [],
  install_requires=[
    'requests'
  ],
)
