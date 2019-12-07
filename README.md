# Remap-interface

Provides a decorator to map interfaces of a class to its member's interfaces.

An alternative way (or a compromise) to solve code-reusing problem when using combination and problems caused by inheriting.
Also, using annonymus fields to replace inheriting with combining seems a bad solution to reuse code (That is still inheriting in my point of view, because the "Diamond Problem" is still there).

This came up to me when I was trying to use combination to replace inheritance.
Remapping interfaces is a dull, annoying, and tiring work for me.

## Usage

```python
import remap_interface.remap as remap

@remap(*args, **kwargs)
# some class
```

Every method in field names in `*args` will be mapped to a class level method, except for magic ones (whose name starts with '__').
If you want to specify the remapping process, do it in `**kwargs`.

Every value inside `*args` and `**kwargs` must be string. After all, before initializing a class, every field inside the class doesn't exist. Seperate fields with a '`.`'.

**If you have explicitly implemented an interface in the class decorated, it will not get overriden.**

### Diamond problem

If there are multiple implementations of an interface to remap in your config, then they will all get disabled silently.

If you want to get a warning or exception on that, this will be a future feature.

If you want those interfaces back, sorry, you must add them manually.

By the way, if there are many implementation conflicts, you'd better rethink your structure.

## Example(s)

```python
@remap('bar', 'bar.__iter__', __len__='bar.__len__')
class Foo:
    def __init__(self):
        self.bar = []

    def index(self, obj):
        print("Nope.")

obj = Foo()
obj.append(1)
obj.extend([2,3])

print(obj.a)
print(len(obj))
for i in obj:
    print(i)
obj.index(3)
```

And you should get the output:

```text
[1, 2, 3]
3
1
2
3
Nope.
```
