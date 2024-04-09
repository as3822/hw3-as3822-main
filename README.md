# Homework 3&nbsp; <a href="/../../pull/1/checks"><img src="/../status/badges/score.svg?raw=true" alt="Latest score" align="right"/></a>

<!-- The above score badge (a) assumes clusterhack-classbot is configured on repos, and (b) relies on relative link to PRs that is *not* officially supported by GitHub -->

The primary goal of this homework is to help you practice writing loops.

---

## Problems


**General caution/hint:** Take care to avoid simple (in hindsight, which is always twenty-twenty :) but time-consuming (in practice, unfortunately) off-by one errors...

More generally, when investigating specific unit test failures and debugging your code, you *should* follow the process that we have been repeatedly using and demonstrating during lectures. Without actually *seeing* the order of operations during execution of your code, it can be *extremely* difficult to find and correct errors.

In this homework assignment, we no longer ask you to write stand-alone apps. Any additional code that you write in order to test and debug your libraries and functions therein (similar to what we have been doing in class) does _not_ need to be committed into your repository (but there should be no harm in doing so). Either way, please make sure to keep that code in separate files (and not in the library modules we ask you to write).


### Problem 1.1 [15pts] &mdash; `list_lib.product`

Define a function called `product` (in `list_lib.py`), which accepts a list of numbers as an argument, and returns the number equal to the product of all elements of the input argument list. For completeness, (a) if the list is empty, your function should return `1`, and (b) the type of the return value should be `float` if at least one of the list elements is a `float`, and `int`
otherwise. Finally, your code should not modify the input list in any way.

**Hint:** Minor variation on the theme of the `total()` problem we worked on during lectures: instead of repeated `+` you need to do a repeated `*`. Also, the additional requirements (a) and (b) given above essentially tell you how to initialize your result variable. As discussed in class, a longer problem description (that explicitly specifies what happens in corner cases, etc) doesn't imply a longer solution (quite often, it's the opposite).

### Problem 1.2 [10pts] &mdash; `stat_lib.geometric_mean`

Define a function `geometric_mean` (in `stat_lib.py`), which accepts a non-empty list of non-negative numbers as an argument, and returns a float equal to the geometric mean of the list’s elements.
Again, your code should not modify the input list in any way. Furthermore, to receive full credit, the
implementation of `stat_lib.geometric_mean` should use the `num_lib.product` function you defined
previously.

**Remark**: As a reminder, the geometric mean $G$ of $n$ numbers, say $x_0, x_1, \ldots, x_{N−1}$ is defined as
$$G := (x_0 \cdot x_1 \cdot\,\cdots\,\cdot x_{N−1})^{\frac{1}{N}}. $$

It is often the appropriate way to "average" values that express relative ratios (e.g., growth rates, or yields).

**Hint:** If you reuse `num_lib.product`, this should be an almost trivial arithmetic expression, since the geometric mean is just the $N$-th root of the product of all $N$ elements of the input list...

### Problem 2.1 [15pts] &mdash; `list_lib.cumsum`

Define a function `list_lib.cumsum` which accepts a list
of numbers (i.e., either floats or ints) and returns a _new_ list that contains the cumulative sums (also known as
the prefix sums) of the input list. Clearly, the returned list should have length equal to the input list (this
includes zero length, of course). Furthermore, you should not modify the input list in any way.

Formally, for any sequence $x_0, x_1, \ldots , x_{N-1}$, the corresponding cumulative sum sequence is defined by
$$cs_0 := x_0, \quad cs_1 := x_0 + x_1,\quad \ldots,\quad cs_{N−1} := x_0 + x_1 + \cdots + x_{N−1}$$

or, generally stated,
$$\mathit{cs}_i := x_0 + x_1 + \cdots + x_i \quad\text{for all $i$ in $0, 1, \ldots, N-1$}. $$

For example, the cumulative sums of `[7, 2, 9]` are `[7, 9, 18]`.

**Suggestion/hint:** You can, effectively, convert the above general statement almost directly into a Python list comprehension expression (noting that $x_0+\cdots+x_{i}$ is `sum(x[0:i+1])` in Python). However, this computes each cumulative sum `cs[i]` "from scratch" each time (i.e., starting to sum from `x[0]` all the way to `x[i]`, inclusive). Instead, you can try to build the `cs` list more efficiently, by using the observation that
$$cs_i = cs_{i-1} + x_i \quad \text{for all $i$ in $1, 2, \ldots, N-1$}.$$

Overall, there are several approaches you can take here (iterating either directly over the elements of `x` or over it's indices, i.e., `range(len(x))`).

### Problem 2.2 [15pts] &mdash; `stat_lib.running_mean`

Define a function `stat_lib.running_mean`,
which accepts a list of numbers as an argument, and returns a _new_ list containing the corresponding
sequence of "running means".

More specifically, for any sequence $x_0, x_1, \ldots, x_{N−1}$ , the corresponding running mean sequence $\mu_0$ , $\mu_1, \ldots, \mu_{N−1}$ is defined by
$$\mu_0 := \frac{x_0}{1}, \quad \mu_1 := \frac{x_0 + x_1}{2},\quad \ldots,\quad \mu_{N−1} := \frac{x_0 + x_1 + \cdots + x_{N−1}}{N}$$

or, generally stated,
$$\mu_i := \frac{x_0 + x_1 + \cdots + x_i}{i+1} \quad\text{for all $i$ in $0, 1, \ldots, N-1$}. $$

For example, the running means of `[7, 2, 9]` are `[7.0, 4.5, 6.0]`.

Clearly, the returned list should contain floats, and should be of the same length as the input argument list.
As always, your code should not modify the input list in any way.

**Hint/suggestion:** Note the similarity to the cumulative sums problem. The main additional "twist" is that you also need the index $i$ in your calculations...

### Problem 3.1 [15pts] &mdash; `fin_lib.daily_returns`

Define a function `fin_lib.daily_rates`,
which accepts a list of (strictly) positive floats as an argument, and returns a new list that which contains
the daily return rates. Clearly, the returned list should have length one less than the input list. If the input’s
length is less than two, you should return an empty list. Finally, your function should not modify the input
list in any way.

For example, the function call `daily_rates([100.0, 80.0, 100.0, 110.0])` should evaluate
to `[-0.2, 0.25, 0.10]`.

More specifically, the $i$-th return rate $r_i$ is defined by
$$r_i := \frac{p_{i+1} − p_i}{p_i} \quad\text{for all $i$ in $0, 1, \ldots, N-2$}.$$

where $p_0, p_1, \ldots p_{N-1}$ is the price sequence given as input.

**Hint:** Can be written as a list comprehension. The code will be easier to write if you iterate over the appropriate range of indices (see the general definition above; it should be possible to "translate" that almost directly into Python...).

### Problem 3.2 [15pts] &mdash; `fin_lib.daily_prices`

Define a function `fin_lib.daily_prices` that is, essentially, the inverse of `fin_lib.daily_rates`. Of course, we can't reconstruct the daily prices just from the daily rates. We also need to know the starting price (and then we can compound the daily rates).

Thus, the `fin_lib.daily_prices` function should accept two input arguments: a start price (float), and a sequence of daily return rates (list of floats).

More specifically, if $s$ is the starting (i.e., first day's) price and $r_0, r_1, \ldots, r_{N-1}$ is the sequence of daily rates (for each day after the first), then the output prices $p_0, p_1, \ldots, p_N$ should be equal to
$$p_0 := s, \quad p_1 := s\cdot (1+r_0), \quad\ldots, \quad p_{N} := s\cdot (1+r_0)\cdot (1+r_1) \cdot\;\cdots\;\cdot (1+r_{N-1})$$

or, generally stated (with the exception of $p_0$),
$$p_i := s\cdot(1+r_0)\cdot(1+r_1)\cdot\;\cdots\;\cdot(1+r_{i-1})\quad\text{for all $i$ in $1, 2, \ldots, N$}.$$

The return value of `fin_lib.daily_prices` should be a _new_ list which contains the corresponding daily price. To be clear, the start price should always be included as the first element of the
returned list (which, therefore, should have length one more than the length of the input list of rates). Again, your function should not modify the input list in any way.

For example, the function call `daily_prices(100.0, [-0.2, 0.25, 0.10])` should evaluate to
`[100.0, 80.0, 100.0, 110.0]` (and, if you compare this to the example for `daily_rates`, you can see the inverse relationship between the two...).

**Hint:** This is a variation on the `cumsum` theme\ldots If you wish, you can implement it most efficiently by observing that
$$p_i = p_{i-1} \cdot (1+r_{i-1}) \quad\text{for all $i$ in $1, 2, \ldots, N$}.$$


### Problem 4 [15pts] &mdash; `list_lib.is_increasing`

Write a function `is_increasing` that accepts a list as an input argument and returns `True` if it's elements are in (strictly) increasing order and `False` otherwise. Once again, your code should _not_ modify the input list in any way.

**Hint:** This is yet another "all-`True`" loop. Specifically, if $x_0, x_1, \ldots, x_{N-1}$ are the list elements, then you need to check that
$$x_{i-1} < x_{i} \quad\text{for all $i$ in $1,2,\ldots,N-1$}.$$

Resist the temptation to resort to something like `sorted(x) == x`. Even though it may produce the correct result, sorting is unnecessary here (not to mention "overkill", as it is _much_ more memory and processor intensive).




