from distutils.core import setup
from distutils.extension import Extension

setup(
    ext_modules = [Extension("force_atlas", ["force_atlas.c"])]
)


