from ibill_parser import IBillParser
from pdf_to_html_converter import PDFToHTMLConverter

PDF_FILE = "sample_ibill.pdf"
CONVERTED_HTML_FILE = "sample_ibill.html"
PDF_CONFIG = "pdf_config\\ibill_config.py"

pdf_converter = PDFToHTMLConverter()
pdf_converter.convert(PDF_FILE, CONVERTED_HTML_FILE)

with open (CONVERTED_HTML_FILE, "r", encoding='utf-8') as file:
    file = file.read()

parser = IBillParser()
parser.feed(file)
parser.set_config(PDF_CONFIG)
parser.set_containers()

print (parser.get_company_name_value())
print (parser.get_company_address_value())
print (parser.get_plan_name_value())

print ("[Account Summary]".center(40, "="))
print (parser.get_account_summary_value("Amount to Pay"))
print (parser.get_account_summary_value("Corporate ID"))
print (parser.get_account_summary_value("Account Number"))
print (parser.get_account_summary_value("Primary Number"))
print (parser.get_account_summary_value("Credit Limit"))
print (parser.get_account_summary_value("Billing Period"))
print (parser.get_account_summary_value("Due Date"))

print ("[Statement Summary]".center(40, "="))
print (parser.get_statement_summary_value("Monthly Plan"))
print (parser.get_statement_summary_value("Add-ons"))
print (parser.get_statement_summary_value("Total"))
print (parser.get_statement_summary_value("Previous Bill Amount"))
KEY = "Remaining Balance (Due immediately)"
print (parser.get_statement_summary_value(KEY))
print (parser.get_statement_summary_value("Amount to Pay"))
