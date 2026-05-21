# Deprecated-Subclass
[![PyPI version](https://badge.fury.io/py/deprecated-subclass.svg)](https://badge.fury.io/py/deprecated-subclass)
![PyPI - Downloads](https://img.shields.io/pypi/dm/deprecated-subclass)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Originally apart of cyares, it is a small library made for the sole purpose of deprecating a class's 
subclassing features without needing to place a `warnings.deprecated` 
wrapper around a  `__init_subclass__` function or needing to define it. 
It also has compatibility for `3.10` and onwards.

```python
from deprecated_subclass import deprecated_subclass

@deprecated_subclass("deprecated because I wanted to.")
class DeprecatedSubclass:
    ...
```



