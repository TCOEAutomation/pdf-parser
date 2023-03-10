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


print ("[Account Summary]".center(40, "="))
print ("Company Name : " + parser.get_company_name_value())
print ("Company Address : " + parser.get_company_address_value())
print ("Plan Value : "  + parser.get_plan_name_value())

parser.print_account_summary_value("Amount to Pay")
parser.print_account_summary_value("Corporate ID")
parser.print_account_summary_value("Account Number")
parser.print_account_summary_value("Primary Number")
parser.print_account_summary_value("Credit Limit")
parser.print_account_summary_value("Billing Period")
parser.print_account_summary_value("Due Date")

print ("[Statement Summary]".center(40, "="))
parser.print_statement_summary_value("Monthly Plan")
parser.print_statement_summary_value("Add-ons")
parser.print_statement_summary_value("Total")
parser.print_statement_summary_value("Previous Bill Amount")
KEY = "Remaining Balance (Due immediately)"
parser.print_statement_summary_value(KEY)
parser.print_statement_summary_value("Amount to Pay")
