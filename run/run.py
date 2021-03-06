from sys import path
import os
path.append(os.path.abspath('../'))


# import function from submodules
# from mod_package.submod1.mod1 import f1
# f1()

# from mod_package.submod2.mod21 import f21
# f21()

# directly import submodules
import mod_package.submod1.mod1 as sb1
sb1.f1()

# call f31 in mod3 from run, this will test addpath within modules
import mod_package.submod3.mod3 as mod3
mod3.f31()
