#from distutils.core import setup
from setuptools import setup

descr = """Tree representations and algorithms for Python.

Viridis is named after the green tree python, Morelia viridis.
"""

DISTNAME            = 'viridis'
DESCRIPTION         = 'Tree data structures and algorithms'
LONG_DESCRIPTION    = descr
MAINTAINER          = 'Juan Nunez-Iglesias'
MAINTAINER_EMAIL    = 'juan.n@unimelb.edu.au'
URL                 = 'https://github.com/jni/viridis'
LICENSE             = 'BSD 3-clause'
DOWNLOAD_URL        = 'https://github.com/jni/viridis'
VERSION             = '0.2-dev'
PYTHON_VERSION      = (2, 7)
INST_DEPENDENCIES   = {} 


if __name__ == '__main__':

    setup(name=DISTNAME,
        version=VERSION,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        license=LICENSE,
        packages=['viridis'],
        package_data={},
        install_requires=INST_DEPENDENCIES,
        scripts=[]
    )

