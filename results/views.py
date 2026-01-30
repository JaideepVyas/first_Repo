from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Result
from examapp.models import Exam
@login_required
def result_list(request):
    results = Result.objects.filter(student=request.user).order_by('-id')

    next_exam = None

    if results.exists():
        last_exam = results.first().exam
        next_exam = Exam.objects.filter(id__gt=last_exam.id).order_by('id').first()

    return render(request, 'results/result_list.html', {
        'results': results,
        'next_exam': next_exam
    })