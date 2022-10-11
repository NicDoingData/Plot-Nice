# TODO: Fill out this file with information about your package

# HINT: Go back to the object-oriented programming lesson "Putting Code on PyPi" and "Exercise: Upload to PyPi"

# HINT: Here is an example of a setup.py file
# https://packaging.python.org/tutorials/packaging-projects/

from setuptools import setup

setup(name = "Plot-Nice",
      version = "1.0",
      description = "Simple wrap for bar, line, and scatter plots"
      packages = ["Plot-Nice"]
      author = "Nicolas Kirsch"
      author_email = "nic.kirsch@outlook.com"
      zip_safe = False)