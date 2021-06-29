from distutils.core import setup
setup(
  name = 'palmettopy',
  packages = ['palmettopy'], # this must be the same as the name above
  version = 'v3.3',
  description = 'Palmetto Python Interface',
  author = 'Ivan Ermilov',
  author_email = 'ivan.s.ermilov@gmail.com',
  url = 'https://github.com/dice-group/palmetto-py', # use the URL to the github repo
  #download_url = 'https://github.com/earthquakesan/palmetto-py/archive/v3.1.tar.gz', 
  keywords = ['aksw', 'nlp', 'semantic-web', 'dice-research', 'topic modeling', 'topic coherence'], # arbitrary keywords
  classifiers = [],
  install_requires=[
    'requests'
  ],
)
