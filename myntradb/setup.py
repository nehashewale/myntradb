from setuptools import setup, find_packages
setup(
      # If name is changed be sure to update the open file path above.
      name = "myntra_db",
      version = "v0.1",
      packages = find_packages(),
      package_dir = {'myntra_db':'myntra_db'},
      author = 'Neha',
      author_email = 'nehashewale3010@gmail.com',
      descipriton = 'Database Layer access used across Myntra',
      license = "PSF",
      include_package_data = True,
      ) 
