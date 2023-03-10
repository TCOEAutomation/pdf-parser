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
parser.print_account_summary_value("Account Number")
parser.print_account_summary_value("Primary mobile number")
parser.print_account_summary_value("Corporate ID")
parser.print_account_summary_value("Bill No.")
parser.print_account_summary_value("Billing Date")
parser.print_account_summary_value("Billing Period")
parser.print_account_summary_value("Due Date")
parser.print_account_summary_value("Credit limit")
parser.print_account_summary_value("No. of Subscribers")

print ("[Statement Summary]".center(40, "="))
parser.print_statement_summary_value("Previous Bill Amount")
parser.print_statement_summary_value("Less: Payments")
parser.print_statement_summary_value("Less: Adjustments")
parser.print_statement_summary_value("Remaining Balance")
parser.print_statement_summary_value("Charges For This Month")
parser.print_statement_summary_value("AMOUNT TO PAY")

print ("[Charges For This Month]".center(40, "="))
parser.print_charges_value("MONTHLY RECURRING FEE")
parser.print_charges_value("EXCESS USAGE")
parser.print_charges_value("OTHER CHARGES")
parser.print_charges_value("ADJUSTMENTS")
parser.print_charges_value("GADGETS AND NON DEVICES")
parser.print_charges_value("TAXES")
parser.print_charges_value("TOTAL")

print ("[Footnote Value]".center(40, "="))
print (parser.get_footnote_value(0))
print (parser.get_footnote_value(1))
print (parser.get_footnote_value(2))

print ("[Subscriptions Value]".center(40, "="))
parser.print_subscriptions_value("Mobile Number")
parser.print_subscriptions_value("MRF")
parser.print_subscriptions_value("Excess Usage")
parser.print_subscriptions_value("Other Charges")
parser.print_subscriptions_value("Gadgets and Non Devices")
parser.print_subscriptions_value("Taxes")
parser.print_subscriptions_value("Total Amount")
