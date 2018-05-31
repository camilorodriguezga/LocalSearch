# LocalSearch

Camilo Andrés Rodríguez Garzón

This is an implementation of the TimeTabling problem.

Requirements
------------
- [copy](https://docs.python.org/2/library/copy.html)
- [matplotlib](https://matplotlib.org/)

Install for linux
-------

```
   sudo make install
```

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

![alt text](https://github.com/camilorodriguezga/Tsp/blob/master/image/greedy/nearestneighbors.gif)

Run
-------

You can run of basic example with:

```
   make
   
   make local_search

```

References
-----------

*  Said Sadiq, Youssei Habib (2000) Iterative Computer Algorithms with Applications in Engineering.
