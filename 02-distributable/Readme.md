## Setup Project Structure With Distribution 

1. All Main package are placed within the src folder.
```
src/ - folder ( not marked with __init__ or __main__ )
   src/pkg  
```

2. A minimal setup.py ( setuptools must be installed )
   ```
   setuptools.setup(
   name="pythonDistribution"
   version="1.0.0",
   description=setuptools.find_packages('src'),
   package_dir={'','src'}
   )
   ```

3. tests placed should use relative imports to python main packages as they are not directly accessible.

## Package Distributions
  - source distribution
     ```
     Containes everything needed to build the packge
      Cannot be placed directly into installation dir.
     ```
  - built distribution
     ```
    Necessary to build the package before installing.
     Placed directly into installation dir
     Can be platform specific
     Build results are included in the package
     ```
    
  - upload to python package index
  
 1. Various formats : zip / tarballs / wheels

#### Standard way for building a SOURCE distribution
1. Passing the sdist argument to setup.py  
  > cd 02-distributable
  > python setup.py sdist
   
2. This creates a new folder 02-distributable/dist with the archive.
3. This archive can be installed on any env as 
   > pip install pythonDistribution-1.0.0

#### Standard way for building a DESTINATION distribution

 1. pip install wheel
 2. python setup.py bdist_wheel
 3. Creates a file in dist/pythonDistribution-1.0.0-py3-none-any.whl
 4. Also creates a build folder
 5. Can be installed on any env as :
   > pip install dist/pythonDistribution-1.0.0-py3-none-any.whl
 6. Additional aspect of where can this pkg be used.
     py3 - python version  
     any - works on any platform  etc 

### Uploading Packages to Python Index.  
   1. Create account to pythonindex
   2. python -m pip install --upgrade twine ( Ensure twine installed for the pip version ) 
      ( utility for publishing python packages )
   3.  twine upload dist/pythonDistribution-1.0.0-py3-none-any.whl 
  
### Installing the package onto any new python env 

  1. mkdir temp  
  2. cd temp  
  3. python -m venv myvenv  
  4. source myvenv/Scripts/activate  
  5. python -m pip install --upgrade pip  
  6. pip install pythonDistribution==1.0.0  
  7. python  
   ```
   >>> from pkg.subpkg.submoduleone import SubOne
   >>> a = SubOne()
   >>> a.say_hello()
   >>> submoduleone.__file__
 'C:\\Installed\\Python310\\lib\\site-packages\\pkg\\subpkg\\submoduleone.py' 
   ```
   