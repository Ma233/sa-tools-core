# coding: utf-8

from io import open
from setuptools import setup, find_packages

version = '0.1.0'


requirements = [
    'setuptools',
    'six',

    # sa-notify
    'wechat @ git+https://github.com/tclh123/wechat.git@py3k#egg=wechat-0.4.17',
    'pycrypto',

    # sa-dns
    'pydnspod @ git+https://github.com/tclh123/pydnspod.git@py3k#egg=pydnspod-0.0.3',

    # sa-script
    'ansible>=2.8',
    'progressbar2',
    'terminaltables',

    # sa-access
    'elasticsearch>=2.0.0,<3.0.0',

    # sa-disk
    'humanize',

    # sa-icinga
    'sentry-sdk',
    'Mako',
    'icinga2-api @ git+https://github.com/tclh123/icinga2-api.git@master#egg=icinga2-api-0.1.0',
    'inflect',
]


entry_points = """
      [console_scripts]
      sa-uptime = sa_tools_core.uptime:main
      sa-dns = sa_tools_core.dns:main
      # sa-node = sa_tools_core.node:main
      # sa-rsync = sa_tools_core.rsync:main
      sa-script = sa_tools_core.script:main
      # sa-lvs = sa_tools_core.lvs:main
      sa-disk = sa_tools_core.disk:main
      sa-notify = sa_tools_core.notify:main
      sa-icinga = sa_tools_core.icinga:main
      sa-access = sa_tools_core.access:main
      sa-bs = sa_tools_core.bs:main
      """

scripts = [
]

setup(name='sa-tools-core',
      version=version,
      description="SA Tools Core",
      long_description=open("README.md", encoding='utf-8').read(),
      # Get more strings from
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: POSIX :: Linux',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      url='https://github.com/douban/sa-tools-core',
      keywords=['sa-tools', 'sysadmin', 'command line tools'],
      author='sysadmin',
      author_email='sysadmin@douban.com',
      license='BSD License',
      packages=find_packages(exclude=['examples*', 'tests*']),
      include_package_data=True,
      zip_safe=False,
      entry_points=entry_points,
      scripts=scripts,

      install_requires=requirements,
)  # NOQA
