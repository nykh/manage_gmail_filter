import xml.etree.ElementTree as ET
import csv
from itertools import chain
import click
import os.path as osp

def prettyPrint(fields):
    """ make the order a bit more intuitive """
    firsts = ["subject", "from", "to"]
    for f in firsts:
        fields.remove(f)
    return firsts + sorted(fields)

@click.command()
@click.argument("filename", type=click.Path(exists=True))
def convertMailFilterXMLtoCSV(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    entries = root.findall("{http://www.w3.org/2005/Atom}entry")
    rows = [{p.get("name"):p.get("value")
        for p in ent.findall("{http://schemas.google.com/apps/2006}property")}
        for ent in entries]

    ofilename = osp.splitext(filename)[0] + '.csv'
    with open(ofilename, "w") as csvfile:
        allfields = set.union(*chain(set(row.keys()) for row in rows))
        dw = csv.DictWriter(csvfile, prettyPrint(allfields))
        dw.writeheader()
        dw.writerows(rows)

convertMailFilterXMLtoCSV()
