# Deprecated-Subclass

Originally apart of cyares, it is a small library made for the sole purpose of deprecating a class's 
subclassing features without needing to place a `warnings.deprecated` 
wrapper around a  `__init_subclass__` function or needing to define it. 
It also has compatability for `3.10` and onwards.

```python
from deprecated_subclass import deprecated_subclass

@deprecated_subclass("deprecated because I wanted to.")
class DeprecatedSubclass:
    ...
```



