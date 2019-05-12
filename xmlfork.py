import os
import sys
import argparse
import datetime
import textwrap
from xml.sax import parse
from xml.sax.saxutils import XMLGenerator

class OutFile(object):
    """Out File Class"""
    def __init__(self, timer, filename, out_folder):
        self.basename, self.ext = os.path.splitext(filename)
        self.outfolder = out_folder
        self.index = 0
        self.openNextFile()

    def openNextFile(self):
        """Open next file"""
        self.index += 1
        if timer is not None:
            print(timer.split('Processing %s at: ' % (self.path())))
        self.file = open(self.path(), 'wb')

    def path(self):
        """Set filename"""
        return '%s%s%s%s' % (self.outfolder, self.basename, self.index, self.ext)

    def start(self):
        """Start file"""
        self.file.close()
        self.openNextFile()

    def write(self, data):
        """Write file"""
        self.file.write(data)

    def close(self):
        """Close file"""
        self.file.close()

class XMLFork(XMLGenerator):
    """Breaker Class"""
    def __init__(self, timer, break_into=None, break_after=1000, out=None, *args, **kwargs):
        XMLGenerator.__init__(self, out, encoding='utf-8', *args, **kwargs)
        self.out_file = out
        self.break_into = break_into
        self.break_after = break_after
        self.context = []
        self.count = 0

    def startElement(self, name, attrs):
        """Start element"""
        XMLGenerator.startElement(self, name, attrs)
        self.context.append((name, attrs))

    def endElement(self, name):
        """End element"""
        XMLGenerator.endElement(self, name)
        self.context.pop()
        if name == self.break_into:
            self.count += 1
            if self.count == self.break_after:
                self.count = 0
                for element in reversed(self.context):
                    self.out_file.write("\n".encode('utf-8'))
                    XMLGenerator.endElement(self, element[0])
                self.out_file.start()
                XMLGenerator.startDocument(self)
                for element in self.context:
                    XMLGenerator.startElement(self, *element)

class Timer(object):
    """Timer class"""
    def __init__(self):
        pass
    
    def init(self, message="Start: "):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        return message + str(self.start)
    
    def terminate(self, message="Total: "):
        """Stops the timer. Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        return message + str(self.stop)
    
    def elapsed(self, message="Elapsed: "):
        """Time elapsed since start was called"""
        return message + str(datetime.datetime.now() - self.start)
    
    def split(self, message="Split started at: "):
        """Start a split timer"""
        self.split_start = datetime.datetime.now()
        return message + str(self.split_start)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Script to divide blocks of a large XML file into several files.',
                                     epilog=textwrap.dedent('''\
                                        Example: 

                                        $ python3 xmlfork.py -f filename.xml -o tmp/ -b blockname_xml -a 10 -n Y'''))
    parser.add_argument("-f", "--filename", type=str, help="filename to be processed", required=True)
    parser.add_argument("-o", "--out_folder", type=str, default='', help="output folder of generated files")
    parser.add_argument("-b", "--block_name", type=str, help="name of the block or label to break the xml", required=True)
    parser.add_argument("-a", "--amount", type=int, default=1, help="amount of block to be processed")
    parser.add_argument("-n", "--notify", type=str, default='N', help="turn on notification")
    args = parser.parse_args()
    timer = args.notify == 'Y' and Timer() or None
    if timer is not None:
        print(timer.init('Process started at: '))
    parse(args.filename, XMLFork(timer, args.block_name, int(args.amount), out=OutFile(timer, args.filename, args.out_folder)))
    if timer is not None:
        print(timer.terminate('Process finalized at: '))
        print(timer.elapsed())