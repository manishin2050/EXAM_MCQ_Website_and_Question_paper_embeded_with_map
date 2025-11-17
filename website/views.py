from django.shortcuts import render,redirect,HttpResponse
from website.models import MCQ_Gen,QuizHeading
# from django.core.files.storage import FileSystemStorage
import gspread
# from datetime import datetime
# import pandas as pd
  # PyMuPDF for PDF text extraction

# Create your views here.
def home(request):
    context={
        "data":QuizHeading.objects.order_by('-id')
    }

    if request.method=="POST":
        name=request.POST.get('name')
        # print(name)
        if name !='':
            Quiz=QuizHeading(name=name)
            Quiz.save()

        return redirect('/')
    return render(request,"home.html",context)

def mehnova_map(request):
    if request.method=="POST":
        ticket_id=request.POST.get('ticket_id')
        indus_id=request.POST.get('indus_id')
        location=request.POST.get('location')
        alarm_generated_time=request.POST.get('alarm_generated_time')
        alarm_cleared_time=request.POST.get('alarm_cleared_time')
        rca=request.POST.get('rca')
        try:
            # 1. Google Sheet Authentication
            import os, traceback
            json_key_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'Ticket_excel_edit.json')
            gc = gspread.service_account(filename=json_key_path)
            # gc = gspread.service_account(filename='static/Ticket_excel_edit.json')
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
            # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # ticket_id = f"TICKET-{datetime.now().strftime('%m%d%H%M%S')}"
            
            new_ticket_data = [
                ticket_id,
                indus_id,
                location,
                alarm_generated_time,
                alarm_cleared_time,
                rca
            ]
            
            # 5. Append new row
            worksheet.append_row(new_ticket_data)
            

        except gspread.exceptions.SpreadsheetNotFound:
            print(f"❌ Error: Spreadsheet '{spreadsheet_name}' not found. Check the sheet name.")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

        return redirect('/mehnova_map')
    return render(request,"loc.html")



def index(request,id):
    context={

        "data":MCQ_Gen.objects.filter(code=id),
        "name":QuizHeading.objects.get(id=id).name,
        "id":id,
    }
    if request.method=="POST":
        que=request.POST.get('que')
        code=id
        ans=request.POST.get('ans')
        opt1=request.POST.get('opt1')
        opt2=request.POST.get('opt2')
        opt3=request.POST.get('opt3')
        opt4=request.POST.get('opt4')
        Data= MCQ_Gen(que=que,code=code,ans=ans,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4)
        Data.save()
        return redirect(f'/index/{id}')
    return render(request,'index.html',context)

def questions(request,id):
    context={
        "data":MCQ_Gen.objects.filter(code=id),
        "name":QuizHeading.objects.get(id=id).name,
        "id":id,
    }
    return render(request,'questions.html',context)

def quiz_delete(request,id):

    QuizHeading.objects.get(id=id).delete()
    for i in MCQ_Gen.objects.filter(code=id):
        i.delete()

    return redirect('/')

def quiz_edit(request,id):
    context={

        "name":QuizHeading.objects.get(id=id).name,
        "id":id,
    }
    if request.method=="POST":
        name=request.POST.get('name')
        Data= QuizHeading(id=id,name=name)
        Data.save()
        return redirect(f'/index/{id}')

    return render(request,"quiz_edit.html",context)

def que_edit(request,id):
    code=MCQ_Gen.objects.get(id=id).code
    # print(code)
    context={
        "name":QuizHeading.objects.get(id=code).name,
        "id":id,
        "que":MCQ_Gen.objects.get(id=id).que,
        "ans":MCQ_Gen.objects.get(id=id).ans,
        "opt1":MCQ_Gen.objects.get(id=id).opt1,
        "opt2":MCQ_Gen.objects.get(id=id).opt2,
        "opt3":MCQ_Gen.objects.get(id=id).opt3,
        "opt4":MCQ_Gen.objects.get(id=id).opt4,
        "code":MCQ_Gen.objects.get(id=id).code,

    }
    if request.method=="POST":
        que=request.POST.get('que')
        code= request.POST.get('code')
        ans=request.POST.get('ans')
        opt1=request.POST.get('opt1')
        opt2=request.POST.get('opt2')
        opt3=request.POST.get('opt3')
        opt4=request.POST.get('opt4')
        Data= MCQ_Gen(id=id,que=que,code=code,ans=ans,opt1=opt1,opt2=opt2,opt3=opt3,opt4=opt4)
        Data.save()
        return redirect(f'/index/{code}')

    return render(request,"que_edit.html",context)

def que_delete(request,id):
    code=MCQ_Gen.objects.get(id=id).code
    MCQ_Gen.objects.get(id=id).delete()
    return redirect(f"/index/{code}")
