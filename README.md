This class will provide an introduction to Python for scientific computing,
with emphasis on statistical applications. In the pilot year, it will be run
as a workshop, and if successful, will be developed into a class for subsequent
years.

Target Audience
---
3rd or 4th year undergraduates, master's students, and 1st or 2nd year PhD
students. The students should have familiarity with programming, but not
necessarily using Python. The intention is to avoid excessive overlap with STA
141 and ECS 10 (basic programming via Python). Completion of one of these two
courses could be recommended or a pre-requisite.

Programming Environment
---
Python 3, since it's starting to be widely adopted. We can recommend a basic
text editor or the free PyCharm IDE (analogous to RStudio) for editing code.

Text
---
There are many excellent, free books available for basic programming in Python.
Most of the packages we'll cover are well-documented and provide examples.
_Python for Data Analysis_ by Wes McKinney might also be a useful reference.

Core Topics
---
+ Python Basics
    * syntax
    * tuples, lists, dicts (and possibly `collections`)
    * list comprehensions
    * iterators (and possibly generators)
    * string manipulation
    * documenting code
+ Numerical computing (`numpy` and `scipy`)
+ Plotting (`matplotlib` or `ggplot`)
+ Statistical methods (`sk-learn`)
+ Data manipulation (`pandas`)

Potential Topics
---
+ IPython
+ File I/O (`io` & `os.path`)
+ Command-line argument parsing (`argparse`)
+ Debugging (`pdb`)
+ Profiling (`timeit` and `cProfile`)
+ Test-driven development (`doctest`)
+ Object-oriented programming
+ Functional programming

Outcomes
---
Students completing the class should understand the following concepts and be able to complete these tasks using Python. They are listed in terms of complexity.

**Advantages of Python**
Since Python is a popular, general purpose language it has many capabilities not shared by domain specific languages like R and Matlab. Python is more likely to be used in production systems. 

**Read the docs**
How to understand Python documentation, ie. what does `**kwargs` mean in a function definition. The benefits of official reviewed docs like [those found in Pandas](http://pandas.pydata.org/pandas-docs/stable/). This enables students to continue their self driven education.

**Use appropriate high level libraries**
Many modules provide similar functionality at different levels of abstraction. One example is [`requests`](http://docs.python-requests.org/en/latest/) compared to `urllib2` for HTTP. High level libraries should be chosen when possible for data analysis tasks.

**Write functions and classes**
Functions and classes are the basic building blocks used to build and organize code. Breaking data analysis tasks down through modular functions provides many benefits.

**Using Pandas effectively**
+ Selecting and filtering rows / columns
+ Understand basic Numpy dtypes and ndarray
+ Missing data, `NAN` values
+ Load data in various formats including CSV, HTML, JSON, XML, HDF5
+ Write CSV
+ `dataframe.str` methods for string processing

**Ipython Notebooks**
Create Ipython notebooks containing the results of analysis. Graph and visualize data. Use LaTeX and Markdown for appropriate formatting. Export to HTML, and optionally to pdf using [pandoc](http://johnmacfarlane.net/pandoc/) and LaTeX.

**Database joins**
Join two different data sets on a common key using Pandas join and merge methods. Understand left, right, inner, and outer joins. This provides functionality comparable to relational databases.

**Group by**
Group data into logical chunks and apply arbitrary functions to those chunks. The pandas `groupby.apply` offers functionality similar to R's apply functions, and in particular resembles `ddply` from [`plyr`](http://plyr.had.co.nz/). This paradigm is used in relational databases and map reduce also.
