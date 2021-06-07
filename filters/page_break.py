"""
Replace $pagebreak with the corresponding HTML for a page-break
"""

from panflute import *
import panflute as pf

def prepare(doc):
    pass
    
def action(elem, doc):
    pass

def finalize(doc):
    doc.replace_keyword("$pagebreak", pf.RawInline('<div style="page-break-before:always;"></div>'))

def main(doc=None):
    return run_filter(action, prepare, finalize, doc=doc) 

if __name__ == '__main__':
    main()
