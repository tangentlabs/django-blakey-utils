import os
from setuptools import setup
from utils import __version__, __author__

setup(name='django-blakey-utils',
    version=__version__,
    url='https://github.com/tangentlabs/django-blakey-utils',
    author=__author__,
    author_email="mariia.sakharova@tangentlabs.co.uk",
    description="Blakey utilities",
    long_description = file(
        os.path.join(
            os.path.dirname(__file__),
            '../README.rst'
        )
    ).read(),
    license='BSD',
    platforms=['linux'],
    packages=['utils', 'utils.re', 'utils.tests'],
    install_requires=
        file(os.path.join(
            os.path.dirname(__file__),
            'deploy/requirements.txt'
        )).read(),
    classifiers = [
        'Development Status :: 1 - Planning',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ],
    zip_safe = False,
)
