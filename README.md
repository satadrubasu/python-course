
#### References :
 Ref : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp    


### Linting and tools ( PEP8 )
  1. pylint --generate-rcfile > mypylintrc ( modify this file as per )
  2. Code level    --  # pylint: disable=invalid-name
  3. pip install black ( black as a commandline tool auto fixes all stylingrelated PEP8 across codebase )
     > black src

### Generating UML Diagrams

1. pip install pylint
2. https://graphviz.org/download/ 
3. pyreverse -o png <path_to_src>


### Documentation Generating HTML documentation ( PEP 257 )

#### 1. docstring ( first line of module/ function / class / method )  
        made available as __doc__ for each of those.  

#### 2.  Sphinx - HTML generator from source documentation  
     reStructuredText -> HTML / PDF   
     > pip install sphinx
     > mkdir docs;cd docs
     > sphinx-quickstart
     > make html  ( will pick the index.rst )
     > configuration stored in config.py
    apidoc = sphinx extension ( Generate docs from python source )  
     > update all doc string in the rst format
     > sphinx-apidoc -o docs mainpkg
     > update the docs/config.py 
     >      extensions = ['sphinx.et.autodoc','sphinx.ext.viewcode'] 
     > cd docs ; make clean html
     
 ### Static Typing in Python  
    Python moving towards type hinting , bettercoding practice.Ide is able to highight and debug in IDE if wrong type is used to call the function etc.Hinting is ignored by the interpreter as such , only helps Pycharm IDE.    
      
    ```
    age: int = 1          ( python 3.6+ )
    age =39  # type: int  ( < python 3.5 )
    def average(a: int, b: int, c: int) -> int:
        return (a+b+c)/3
    ```
     
