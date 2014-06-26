# Python for Data Mining
Messy data has an inconsistent or inconvenient format, 
and may have missing values.
Noisy data has measurement error.
_Data mining extracts meaningful information from messy, noisy data._
This is a multi-step process which includes gathering, cleaning, visualizing,
modeling, and reporting.

This course provides an introduction to Python,
with emphasis on data mining and other statistical applications.
Students who finish the class should understand the following concepts (listed
by complexity) and be able to complete relevant tasks using Python. 

**Uses of Python:**
[Python](http://en.wikipedia.org/wiki/Python_language) is a high-level
programming language in widespread use.
Although it's a general-purpose language, it's important to recognize its
strengths and weaknesses.

**Reading and Writing Docs:**
Being able to read code documentation empowers students to educate themselves.
This entails developing a new vocabulary, e.g., what `**kwargs` means in a
function definition. 

Writing code documentation is equally important, especially in collaborative
projects.
Consider the benefits of official docs like 
[those found in Pandas](http://pandas.pydata.org/pandas-docs/stable/). 

**Reporting Results:**
The results of data analysis should be presented in a clear, reproducible way.
IPython notebooks make it easy to combine writing, visualizations, and code.

+ Writing should be more than just a summary. Critical thinking is essential!
+ Graphs should be well-labelled, and convey information of interest without
  clutter.
+ Use LaTeX or Markdown for appropriate formatting. Export to HTML, and
  optionally to PDF using [pandoc](http://johnmacfarlane.net/pandoc/) and
  LaTeX.

**Code Organization:**
Functions and classes are the basic building blocks used to organize code. 
Breaking data analysis tasks into small, modular steps makes code easier to
read, write, test, and reuse.

**Database Queries:**
Join two different data sets on a common key using join and merge methods. 
Understand left, right, inner, and outer joins.

**Numerical Computing:**
Efficiency and numerical stability are essential to any algorithm.
NumPy's n-dimensional arrays (ndarray) support fast vectorized operations.
NumPy and SciPy provide much of the same functionality as R's built-in
functions.

**Effective pandas Use:**
The pandas module is a good foundation for most data analyses.

+ Select and filter rows / columns
+ Read various formats including CSV, HTML, JSON, XML, HDF5
+ Write CSVs
+ Handle missing data, or `NaN`s
+ Process strings, with methods such as `dataframe.str`
+ Use group-by operations, such as `groupby.apply`, which resembles R's apply
  functions and `ddply` from [`plyr`](http://plyr.had.co.nz/)

**Appropriate Abstraction:**
Many libraries provide similar functionality at different levels of
abstraction. One example is 
[`requests`](http://docs.python-requests.org/en/latest/) 
compared to `urllib2` for HTTP.
High level libraries should be chosen when possible for data analysis tasks.

## Target Audience
3rd or 4th year undergraduates, master's students, and 1st or 2nd year PhD
students. The students should have familiarity with programming, but not
necessarily using Python. The intention is to avoid excessive overlap with STA
141 and ECS 10 (basic programming via Python). Completion of one of these two
courses could be recommended or a pre-requisite.

## Programming Environment
Python 3 has syntax changes and new features that break compatibility with
Python 2.
All of the major scientific computing libraries have added support for Python 3
over the last few years, so it will be our focus.
We recommend the [Anaconda][] Python 3 distribution,
which bundles most packages we'll use into one download.
Any other packages needed can be installed using `pip` or `conda`.

Python code is supported by a vast array of editors.

+ [Spyder IDE][Spyder], included in Anaconda, 
  is a Python equivalent of RStudio, 
  designed with scientific computing in mind.
+ [PyCharm IDE][PyCharm] has very well-designed user interface. Chris uses
  PyCharm.
+ General-purpose text editors, such as [Vim][] and [Emacs][], are a great
  choice for ambitious students. They can be used with any language. 
  See [here][Text Editors] for more details. Clark and Nick both use Vim.

[Anaconda]: http://continuum.io/downloads
[Spyder]: https://code.google.com/p/spyderlib/
[PyCharm]: https://www.jetbrains.com/pycharm/
[Vim]: http://www.vim.org/
[Emacs]: https://www.gnu.org/software/emacs/
[Text Editors]: http://heather.cs.ucdavis.edu/~matloff/ProgEdit/ProgEdit.html

## References
The main reference text will be Wes McKinney's book

+ McKinney, W. (2012). _Python for Data Analysis: Data Wrangling with Pandas, 
  NumPy, and IPython_. O'Reilly Media.

General purpose references include

+ Lutz, M. (2014). _Python Pocket Reference_. O'Reilly Media. 
+ Beazley, D. (2009). _Python Essential Reference_. Addison-Wesley.
+ Pilgrim, M., & Willison, S. (2009). _[Dive Into Python 3][]_. Apress.
+ [StackOverflow][]. Please be conscious of the [rules][SO Rules]!

There are also many free online resources for learning to program in Python:

+ [Non-programmer's Tutorial for Python 3][Non]
+ [Beginner's Guide to Python][Beginner's Guide]
+ Swaroop, C. H. (2003). _[A Byte of Python][]_.
+ Reitz, K. _[Hitchhiker's Guide to Python][Hitchhiker's Guide]_
  ([PDF][Hitchhiker's PDF]).
+ [Five Lifejackets to Throw to the New Coder][New Coder]
+ [Pyvideo][Pyvideo]. Recommended speakers include Guido Van Rossum,
  Raymond Hettinger, Travis Oliphant, Fernando Perez, David Beazley, and Alex
  Martelli.

Moreover, most of the packages we'll cover have excellent documentation:

+ [Python 3](https://docs.python.org/3/) (including the standard library)
+ [NumPy](http://docs.scipy.org/doc/numpy/)
+ [SciPy](http://docs.scipy.org/doc/scipy/reference/)
+ [matplotlib](http://matplotlib.org/contents.html)
+ [pandas](http://pandas.pydata.org/pandas-docs/stable/)
+ [IPython](http://ipython.org/documentation.html)
+ [scikit-learn](http://scikit-learn.org/stable/documentation.html)

[A Byte of Python]: http://www.swaroopch.com/notes/python/
[Dive Into Python 3]: http://www.diveintopython3.net/
[Non]: http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3
[Beginner's Guide]: https://wiki.python.org/moin/BeginnersGuide
[New Coder]: http://newcoder.io/
[Hitchhiker's Guide]: http://docs.python-guide.org/en/latest/
[Pyvideo]: http://pyvideo.org/
[Hitchhiker's PDF]: https://media.readthedocs.org/pdf/python-guide/latest/python-guide.pdf
[StackOverflow]: http://stackoverflow.com/questions/tagged/python
[SO Rules]: http://stackoverflow.com/tour

## Topics
The core topics will be

+ Python Basics
    * syntax
    * tuples, lists, dicts (and possibly `collections`)
    * list comprehensions
    * iterators (and possibly generators)
    * string manipulation
    * documenting code
+ Numerical computing (`numpy` and `scipy`)
+ IPython
+ Plotting (`matplotlib` or `ggplot`)
+ Data manipulation (`pandas`)
+ Web-scraping (`requests` and `bs4`)

Other topics we may cover include

+ File I/O (`io` and `os.path`)
+ Command-line argument parsing (`argparse`)
+ Debugging (`pdb`)
+ Profiling (`timeit` and `cProfile`)
+ Test-driven development (`doctest`)
+ Object-oriented programming
+ Functional programming
+ Statistical methods (`sklearn`)
+ Database queries
