# setup.py, config file for distutils

import UnRAR2

from distutils.core import setup
from distutils.command.install_data import install_data
import os


class smart_install_data(install_data):
    def run(self):
        #need to change self.install_dir to the actual library dir
        install_cmd = self.get_finalized_command('install')
        self.install_dir = getattr(install_cmd, 'install_lib')
        return install_data.run(self)


data_files = []
for dirpath, dirnames, filenames in os.walk(r'..\UnRAR2'):
    for dirname in ['build', 'dist', '_sgbak']:
        try:
            dirnames.remove(dirname)
        except ValueError:
            pass
    for filename in [fn for fn in filenames if os.path.splitext(fn)[-1].lower() in ('.pyc', '.pyo', '.scc')]:
        filenames.remove(filename)
    data_files.append((dirpath.lstrip('.').lstrip('\\'), [os.path.join(dirpath, fn) for fn in filenames]))


setup(name='pyUnRAR2',
      version=UnRAR2.__version__,
      description='Improved Python wrapper around the free UnRAR.dll',
      long_description=UnRAR2.__doc__.strip(),
      author='Konstantin Yegupov',
      author_email='yk4ever@gmail.com',
      url='http://code.google.com/py-unrar2',
      license='MIT',
      platforms='Windows',
      classifiers=[
                   'Development Status :: 4 - Beta',
                   'Environment :: Win32 (MS Windows)',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: Microsoft :: Windows',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: System :: Archiving :: Compression',
                  ],
      packages=['UnRAR2'],
      package_dir={'UnRAR2' : ''},
      data_files=data_files,
      cmdclass = {'install_data': smart_install_data},
     )
