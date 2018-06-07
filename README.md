auto_pdb
--

This module enables automatically starting [pdb](https://docs.python.org/3/library/pdb.html) debugging when an error occurs.

## Example

```example.py
import auto_pdb

with auto_pdb.trap(confirm=False):
    x = list(range(2))
    y = x[3]
```

```
$ python example.py
Traceback (most recent call last):
  File "example.py", line 5, in <module>
    y = x[3]
IndexError: list index out of range

> example.py(5)<module>()
-> y = x[3]
(Pdb)
```

## Installation

```sh
pip install git+https://github.com/raahii/auto_pdb.git
```
