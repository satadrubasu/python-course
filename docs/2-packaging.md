Pypi packaging  

pip install


### Create own Modules and Packages of Modules.
 Modules - .py that u call in another py
 Packages - collection of modules 
 
mymodule.py
program.py 
 
from mymodule import my_func

```
[MainPackageFolder]
  |--- __init__.py
  |--- [SubPackageFolder]
  |      |-- __init__.py
  |      |-- sub_module.py
  |--- main_module.py
 

from MainPackageFolder import main_module
from MainPackageFolder.SubPackageFolder import sub_module

sub_module.function_print()
```


### name and main
 If a modules function is being used as an import or using the original .py file of that module.  
```
if __name__== "__main__"

```
 > python one.py
    
When run from command line by firing python - > internally __name__ is assigned "__main__"  

   BUT

When run by importing from another python  
```
# two.py
import one
one.func()
```