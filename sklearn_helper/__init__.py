from os.path import dirname, basename, isfile, join
import glob

# find the absolute path of all .py files in package dir
modules = glob.glob(join(dirname(__file__), "*.py"))

# set each as export in from package import *
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

# expose modules for downstream import
from . import *

# https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder/20753073#20753073
# https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html