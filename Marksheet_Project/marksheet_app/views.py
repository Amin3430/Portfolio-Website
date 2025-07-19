from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def index(request):
    return render(request, 'form.html')

def submit_marksheet(request):
    if request.method == 'POST':
        data = request.POST
        marks = {
            'math': int(data['math']),
            'english': int(data['english']),
            'science': int(data['science']),
            'physics': int(data['physics']),
            'chemistry': int(data['chemistry']),
            'computer': int(data['computer']),
        }
        total = sum(marks.values())
        percentage = round(total / len(marks), 2)
        result = 'Pass' if all(m >= 35 for m in marks.values()) else 'Fail'
        grade = 'A+' if percentage >= 90 else 'A' if percentage >= 80 else 'B' if percentage >= 70 else 'C' if percentage >= 60 else 'D' if percentage >= 50 else 'F'
        student = {'name': data['name'], 'roll_number': data['roll_number'], **marks, 'total': total, 'percentage': percentage, 'result': result, 'grade': grade}
        request.session['student_data'] = student
        return render(request, 'marksheet.html', {'student': student})

def download_pdf(request):
    student = request.session.get('student_data')
    html = render_to_string('marksheet.html', {'student': student})
    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Marksheet_{student["roll_number"]}.pdf"'
    return response
