## Installation

To install on a *nix system:

<pre><code>$ python setup.py install</code></pre>

If you have tox installed on your system you can use it to automate the creation of a virtualenv and run the unittests

<pre><code>$ tox </code></pre>

This will create a python 3 virtualenv.  You can activate it by running:

<pre><code>$ source .tox/py3/bin/activate</code></pre>

## word-count.py

You can use this utility from the command line to either process a string or a file

<pre><code>$ word-count.py --string "lorem ipsum lorem"</code></pre>

should output

<pre><code>{'lorem': 2, 'ipsum': 1}</pre></code>

You can also process a text file using the file switch

## meeting-times.py

To condense integer or unix timestamp meeting times

<pre><code>$ meeting-times.py --meeting 1,4 3,6 2,5  </code></pre>

for iso 3601 timestamps

<pre><code>$ meeting-times.py --string_meeting 2010-05-08T00:41:54.000000Z,2010-05-08T01:41:54.000000Z 2010-05-08T02:41:54.000000Z,2010-05-08T05:41:54.000000Z  </code></pre>


## Tests

All unit tests are in meeting_times_test.py and wordcount_test.py


## Additional Notes

Initially I tried to parallelize word count using the multiprocessing module but I wasn't getting any performance gains, even on large files. I suspect this is due to how expensive it is to aggregate the results
