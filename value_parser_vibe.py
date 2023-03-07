from vibe_parser import VibeParser
from pdf_to_html_converter import PDFToHTMLConverter

PDF_FILE = "sample_vibe.pdf"
CONVERTED_HTML_FILE = "sample_vibe.html"
PDF_CONFIG = "pdf_config\\vibe_config.py"

pdf_converter = PDFToHTMLConverter()
pdf_converter.convert(PDF_FILE, CONVERTED_HTML_FILE)
with open (CONVERTED_HTML_FILE, "r", encoding='utf-8') as file:
    file = file.read()

parser = VibeParser()
parser.feed(file)
parser.set_config(PDF_CONFIG)
parser.set_containers()

print ("[Account Summary]".center(40, "="))
print (parser.get_account_summary_value("Account Number"))
print (parser.get_account_summary_value("Primary mobile number"))
print (parser.get_account_summary_value("Corporate ID"))
print (parser.get_account_summary_value("Bill No."))
print (parser.get_account_summary_value("Billing Date"))
print (parser.get_account_summary_value("Billing Period"))
print (parser.get_account_summary_value("Due Date"))
print (parser.get_account_summary_value("Credit limit"))
print (parser.get_account_summary_value("No. of Subscribers"))

print ("[Statement Summary]".center(40, "="))
print (parser.get_statement_summary_value("Previous Bill Amount"))
print (parser.get_statement_summary_value("Less: Payments"))
print (parser.get_statement_summary_value("Less: Adjustments"))
print (parser.get_statement_summary_value("Remaining Balance"))
print (parser.get_statement_summary_value("Charges For This Month"))
print (parser.get_statement_summary_value("AMOUNT TO PAY"))

print ("[Statement Summary]".center(40, "="))
print (parser.get_charges_value("MONTHLY RECURRING FEE"))
print (parser.get_charges_value("EXCESS USAGE"))
print (parser.get_charges_value("OTHER CHARGES"))
print (parser.get_charges_value("ADJUSTMENTS"))
print (parser.get_charges_value("GADGETS AND NON DEVICES"))
print (parser.get_charges_value("TAXES"))
print (parser.get_charges_value("TOTAL"))

print ("[Footnote Value]".center(40, "="))
print (parser.get_footnote_value(0))
print (parser.get_footnote_value(1))
print (parser.get_footnote_value(2))

print ("[Subscriptions Value]".center(40, "="))
print (parser.get_subscriptions_value("Mobile Number"))
print (parser.get_subscriptions_value("MRF"))
print (parser.get_subscriptions_value("Excess Usage"))
print (parser.get_subscriptions_value("Mobile"))
print (parser.get_subscriptions_value("Other Charges"))
print (parser.get_subscriptions_value("Gadgets and Non Devices"))
print (parser.get_subscriptions_value("Taxes"))
print (parser.get_subscriptions_value("Total Amount"))