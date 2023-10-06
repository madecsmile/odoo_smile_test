from distutils.core import setup
setup(
  name = 'odoo-smile_test',
  packages = ['smile_test'],
  version = '16.0.0',
  license='LGPL',
  description = 'Smile test module',
  author = 'Smile',
  author_email = 'martin.deconinck@smile.fr',
#   url = 'https://github.com/to/do',
  download_url = 'https://filebin.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['odoo', 'test', 'smile_test', 'smile'],
  install_requires=[            # I get to this in a second
          'coverage',
          'flake8',
          'unittest2',
          'pycobertura',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: LGPL License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)