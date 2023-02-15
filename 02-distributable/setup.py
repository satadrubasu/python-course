import setuptools

setuptools.setup(
   name="pythonDistribution",
   version="1.0.0",
   description="Skeleton for setuptools and project structure",
   packages=setuptools.find_packages('src'),
   package_dir={'':'src'}
   )