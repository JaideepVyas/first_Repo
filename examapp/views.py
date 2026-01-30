from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
from results.models import Result


@login_required
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'examapp/exam_list.html', {
        'exams': exams
    })


@login_required
def start_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = Question.objects.filter(exam=exam)

    # prevent retake (optional but recommended)
    if Result.objects.filter(student=request.user, exam=exam).exists():
        return redirect('result_list')

    if request.method == "POST":
        score = 0

        for question in questions:
            selected = request.POST.get(f"question_{question.id}")

            if selected == question.correct_option:
                score += 1

        Result.objects.create(
            student=request.user,
            exam=exam,
            score=score
        )

        return redirect('result_list')

    return render(request, 'examapp/start_exam.html', {
        'exam': exam,
        'questions': questions
    })