# XMLFork

Script to divide blocks of a large XML file into several files with Python.

> Built and tested with Python 3.7+

## Install

Please use virtualenv if you don't want to add dependencies to your global python install: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Usage

```sh
$ python3 xmlfork.py -f filename.xml -o tmp/ -b blockname_xml -a 1000 -n Y

Process started at: 2019-05-11 19:31:41.004876
Processing tmp/filename1.xml at: 2019-05-11 19:31:41.004968
Processing tmp/filename2.xml at: 2019-05-11 19:32:03.874401
Processing tmp/filename3.xml at: 2019-05-11 19:32:25.517026
Processing tmp/filename4.xml at: 2019-05-11 19:32:34.820695
Processing tmp/filename5.xml at: 2019-05-11 19:32:53.196072
Processing tmp/filename6.xml at: 2019-05-11 19:33:08.940740
Processing tmp/filename7.xml at: 2019-05-11 19:33:21.722749
Processing tmp/filename8.xml at: 2019-05-11 19:33:33.285519
Process finalized at: 2019-05-11 19:33:55.183420
```

Options:

`$ python3 xmlfork.py -h`

```sh
usage: xmlfork.py [-h] -f FILENAME [-o OUT_FOLDER] -b BLOCK_NAME
                      [-a AMOUNT] [-n NOTIFY]

Break large XML file

optional arguments:
  -h, --help                              show this help message and exit
  -f FILENAME, --filename FILENAME        filename to be processed
  -o OUT_FOLDER, --out_folder OUT_FOLDER  output folder of generated files
  -b BLOCK_NAME, --block_name BLOCK_NAME  name of the block or label to break the xml
  -a AMOUNT, --amount AMOUNT              amount of block to be processed
  -n NOTIFY, --notify NOTIFY              turn on notification

Example:

$ python3 xmlfork.py -f filename.xml -o tmp/ -b blockname_xml -a 1000 -n Y
```

Note: The sample xml file is not included.

Author

- Alvaro Vega Plata