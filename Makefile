
all: clean .ve2
	.ve2/bin/python setup.py install

.ve2:
	virtualenv -p python2 .ve2

clean:
	rm -fr dist build *.egg-info
	find . -name __pycache__ -o -name \*.pyc | xargs rm -fr
	tree .
