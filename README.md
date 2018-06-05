# LocalSearch

Camilo Andrés Rodríguez Garzón

This is an implementation of Local Search for solved TimeTabling problem.

Requirements
------------
- [copy](https://docs.python.org/2/library/copy.html)
- [matplotlib](https://matplotlib.org/)

### Testing

The module can test for

`TimeTabling Local Search with:`

you can add the following entries to the program with the following order in mind:

* file name
* maximum number of Neighbors

```
   python localsearch.py

   python localsearch.py timetabling1.csv

   python localsearch.py timetabling1.csv 200
```

### Examples
```
python localsearch.py
```

![alt text](https://github.com/camilorodriguezga/LocalSearch/blob/master/img/out.png)

Run
-------

You can run of basic example with:

```
   make
   
   make local_search

   make file="namefile.extension"

   make file="namefile.extension"  neighbors="numberneighbors"

```

References
-----------

*  Said Sadiq, Youssei Habib (2000) Iterative Computer Algorithms with Applications in Engineering.
