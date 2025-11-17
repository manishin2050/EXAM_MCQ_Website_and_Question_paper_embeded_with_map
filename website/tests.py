from django.test import TestCase

# Create your tests here.
import gspread
from datetime import datetime
import pandas as pd

def add_new_ticket_to_sheet(issue_description, customer_name, priority):
    try:
        # 1. Google Sheet Authentication
        gc = gspread.service_account(filename='static/Ticket_excel_edit.json')
        print("✅ Authentication Successful.")
        
        # 2. Open Spreadsheet and Worksheet
        spreadsheet_name = 'Ticket Handler'
        worksheet_name = 'Sheet1'
        sh = gc.open(spreadsheet_name)
        worksheet = sh.worksheet(worksheet_name)
        
        # 3. Check if headers are already present
        existing_data = worksheet.get_all_values()
        
        headers = ["Ticket ID", "Indus ID", "Location", "Alarm Generated Time", "Alarm Cleared Time","RCA"]
        
        if not existing_data:
            worksheet.append_row(headers)
            print("🧾 Headers added to empty sheet.")
        elif existing_data[0] != headers:
            worksheet.delete_rows(1)   # purane headers hatao
            worksheet.insert_row(headers, 1)  # naye headers lagao
            print("🔄 Headers automatically updated.")
        # 4. Generate Ticket Info
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ticket_id = f"TICKET-{datetime.now().strftime('%m%d%H%M%S')}"
        
        new_ticket_data = [
            ticket_id,
            customer_name,
            issue_description,
            priority,
            timestamp
        ]
        
        # 5. Append new row
        worksheet.append_row(new_ticket_data)
        
        print("-" * 40)
        print(f"🎉 New Ticket Added:")
        print(f" ID: {ticket_id}")
        print(f" Customer: {customer_name}")
        print(f" Issue: {issue_description}")
        print(f" Priority: {priority}")
        print(f" Time: {timestamp}")
        print("-" * 40)

    except gspread.exceptions.SpreadsheetNotFound:
        print(f"❌ Error: Spreadsheet '{spreadsheet_name}' not found. Check the sheet name.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


# --- Example Usage ---
add_new_ticket_to_sheet(
    issue_description="This is coming from my code ",
    customer_name="Manish Kumar",
    priority="High"
)				
# उदाहरण 2 (कुछ देर बाद जब दूसरा टिकट बना):
# add_new_ticket_to_sheet(
# issue_description="Request for new laptop setup.",
# customer_name="Priya Sharma",
# priority="Medium"
# )						
