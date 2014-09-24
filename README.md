# Python for Data Mining

[Python][] is a programming language designed to have clear, concise, and
expressive code.
An extremely popular general-purpose language, Python has been used for tasks
as diverse as web development, teaching, and systems administration.
This workshop provides an introduction to Python for data mining.

Messy data has an inconsistent or inconvenient format, and may have missing
values.
Noisy data has measurement error.
*Data mining extracts meaningful information from messy, noisy data.*
This is a start-to-finish process that includes gathering, cleaning,
visualizing, modeling, and reporting.

Programming and research best practices are a secondary focus of the workshop,
because [Python is a philosophy][zen] as well as a language.
Core concepts include: writing organized, well-documented code; being a
self-sufficient learner; using version control for code management and
collaboration; ensuring reproducibility of results; producing concise,
informative analyses and visualizations.

The workshop will meet for four weeks during the Winter 2015 quarter at the
University of California, Davis.

[zen]: http://legacy.python.org/dev/peps/pep-0020/
[Python]: https://www.python.org/

## Target Audience
The workshop is open to undergraduate and graduate students from all
departments.
We recommend that students have prior programming experience
and a basic understanding of statistical methods,
so they can follow along with the examples.
For instance, completion of STA 108 and STA 141 is sufficient
(but not required).

The statistics department's Spring 2015 machine learning course, STA 208, will
be language agnostic, so we encourage students who attend this workshop to
practice their Python skills again in Spring!

## Topics

**Python Basics:**

**Numerical Computing:**
Efficiency and numerical stability are essential to any algorithm.
NumPy's n-dimensional arrays (ndarray) support fast vectorized operations.
NumPy and SciPy provide much of the same functionality as R's built-in
functions.

**Data Manipulation:**
The pandas module duplicates many of the features (and some of the flaws) of
R's data.frames. This module is especially useful for data manipulation
such as:

+ Filtering and restructuring data
+ Reading and writing CSVs
+ Handling missing values
+ Performing group-by operations, such as `groupby.apply`,
  which resembles R's apply functions and `ddply` from 
  [plyr](http://plyr.had.co.nz/)

**Data Visualization:**

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
  PyCharm with the IdeaVim Vi plugin.
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

Documentation for Python and various packages can be found at the following
links:

+ [Python 3](https://docs.python.org/3/)
+ [NumPy](http://docs.scipy.org/doc/numpy/)
+ [SciPy](http://docs.scipy.org/doc/scipy/reference/)
+ [matplotlib](http://matplotlib.org/contents.html)
+ [pandas](http://pandas.pydata.org/pandas-docs/stable/)
+ [IPython](http://ipython.org/documentation.html)
+ [scikit-learn](http://scikit-learn.org/stable/documentation.html)

Although it's not required for the workshop, we also encourage students to take
a look at Wes McKinney's very relevant book:

+ McKinney, W. (2012). _Python for Data Analysis: Data Wrangling with Pandas, 
  NumPy, and IPython_. O'Reilly Media.

General purpose references include:

+ Lutz, M. (2014). _Python Pocket Reference_. O'Reilly Media. 
+ Beazley, D. (2009). _Python Essential Reference_. Addison-Wesley.
+ Pilgrim, M., & Willison, S. (2009). _[Dive Into Python 3][]_. Apress.
+ [StackOverflow][]. Please be conscious of the [rules][SO Rules]!

Finally, there are many free resources for learning Python online:

+ [Non-programmer's Tutorial for Python 3][Non]
+ [Beginner's Guide to Python][Beginner's Guide]
+ Swaroop, C. H. (2003). _[A Byte of Python][]_.
+ Reitz, K. _[Hitchhiker's Guide to Python][Hitchhiker's Guide]_
  ([PDF][Hitchhiker's PDF]).
+ [Five Lifejackets to Throw to the New Coder][New Coder]
+ [Pyvideo][Pyvideo]. Recommended speakers include Guido Van Rossum,
  Raymond Hettinger, Travis Oliphant, Fernando Perez, David Beazley, and Alex
  Martelli.


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

