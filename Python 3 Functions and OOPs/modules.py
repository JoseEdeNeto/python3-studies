import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

import sys; print(sys.builtin_module_names)
import builtins; print(builtins.dict.keys())