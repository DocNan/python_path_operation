toc
Only with path operation, could you call your self-defined modules.

# basic path operation

## get absolute path
```
import os
os.path.abspath('../')
```

This will get the absolute path relative to current directory.


## add path to search directory
```python
import sys
sys.path.append('/home/jake/Documents')
```


# addpath within module

## module definition
python module is identified with special file __init__.py. Within this file, the content is defined as:
```
__all__ = ['module1', 'module2']
```


## add relative path within module
Suppose we have a module structure like this:
```
/module/module1/mod1.py
# mod1.py contains function f1()
/module/module2/mod2.py
# mod2.py contains function f2()
# f2() will call f1() in mod1.py
/module/run.py
# run.py will call f2()
```

Which means in order to call f1() within f2(), mod2.py must add mod1.py to its serach path. But the execute function is located within the positon of /module/run.py, which means we can addpath this path in run.py, which is the current directory. To add path within mod2.py, simple script is like this:
```
from ..module1 import mod1
def f2():
    mod1.f1()
f2()
```

And within any subdirectory of /module/, __init__.py should all be added.


# other operation

You can use the above code to add a directory to the current directory. To call a module in this directory, eg: /home/jake/Documents/catchfish.py

You can use these code:

```python
import catchfish
# then you can use any function in this module like this:
catchfish.cat(3)
catchfish.dog(0)
```

Or if just wish to use one function from this module you can do this:

```python
from catchfish import cat
from catchfish import dog
# then use the functions like this.
cat(3)
dog(0)
```


## rename imported function

```
from catchfish import cat as f1
from catchfish import dog as f2
# then you can use them like this:
f1(3)
f2(0)
```
