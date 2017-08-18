import xml.etree.ElementTree as ET
import csv
from itertools import chain
import click
import os.path as osp

head = """<?xml version='1.0' encoding='UTF-8'?><feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
	<title>Mail Filters</title>
	<id></id>
	<updated></updated>
	<author>
		<name>Blah</name>
		<email>blah@sumologic.com</email>
	</author>\n"""
entry_head = """		<category term='filter'></category>
    <title>Mail Filter</title>
    <id></id>
    <updated></updated>
    <content></content>\n"""
tail = "</feed>\n"

def escaped(s):
	return s.replace("<", "&lt;").replace(">", "&gt;")

@click.command()
@click.argument("filename", type=click.Path(exists=True))
def convertMailFilterCSVtoXML(filename):
    with open(filename) as csvfile:
        dr = csv.DictReader(csvfile)

        ofilename = osp.splitext(filename)[0] + '.xml'
        with open(ofilename, "w") as xmlfile:
            xmlfile.write(head)
            for ent in dr:
                xmlfile.write("\t<entry>\n")
                xmlfile.write(entry_head)
                for k, v in ent.items():
                    if not v: continue
                    xmlfile.write(f"\t\t<apps:property name='{k}' value='{escaped(v)}'/>\n")
                xmlfile.write("\t</entry>\n")
            xmlfile.write(tail)

convertMailFilterCSVtoXML()
