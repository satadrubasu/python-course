

## Locating Modules while importing

- Python checks the sys.path list in order


1.  Modifying sys.path:  
    and append On Repl:  
    > import sys
    > sys.path.extend(['01-organizing'])
    > from pkg import sample
 
2.  Modify PYTHONPATH
    Windows:  
    >  set PYTHONPATH=C:\\Dev\\external\\python-play\\01-organizing;path2;


## Executable Directories 
Concept: when a dir has __main__.py , its added to the sys.path  
  1.  '01-organizing' is a folder of no pythonic value    
  2.  __main__.py is placed under the 01-organizing folder to make this folder as executable  
  3. pkg (folder) has __init__.py  
  4. subpkg (folder) also has __init__.py    
  5. Note relative imports used in mainentry.py  
     > from .subpkg.submoduleone import SubOne 

 To Execute :
  1.  Open Terminal for project at python-play.   
     
     > python 01-organizing 

 
  
## Executable Zip
  Concept : In continuation of the above executable directory , a zip file should not contain the dir but the contents of the directory.

  > cd 01-organizing
  > python -m zipfile -c ../organizing.zip .
  > cd ..
  > ls organizing.zip
  > python organizing.zip


###  Executable Packages
