from distutils.core import setup
setup(
  name = 'palmettopy',
  packages = ['palmettopy'], # this must be the same as the name above
  version = 'v1.0',
  description = 'Palmetto Python Interface',
  author = 'Ivan Ermilov',
  author_email = 'ivan.s.ermilov@gmail.com',
  url = 'https://github.com/earthquakesan/palmetto-py', # use the URL to the github repo
  download_url = 'https://github.com/earthquakesan/palmetto-py/archive/v1.0.tar.gz', 
  keywords = ['aksw', 'nlp', 'semantic-web'], # arbitrary keywords
  classifiers = [],
  install_requires=[
    'requests'
  ],
)
