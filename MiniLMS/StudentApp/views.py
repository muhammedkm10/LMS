from django.shortcuts import render, redirect
from AuthApp.decorator import (
    check_session_key,
    check_student_session,
    check_teacher_session,
)
from django.views.decorators.cache import never_cache
from TeacherApp.models import Courses, Quiz
from .models import QuizSubmissionDetails
from django.http import JsonResponse
import random
from AuthApp.models import CustomUser
from django.utils import timezone


# student home
@check_session_key("email")
@check_student_session
@never_cache
def StudentHome(request):
    # if user went back to the home from the quiz clearing the session
    request.session.pop("quiz_answers", None)
    courses_with_teachers = Courses.objects.select_related("teacher").all()
    email = request.session["email"]
    user = CustomUser.objects.get(email=email)

    # Retrieve all submission details for the user

    submissions = QuizSubmissionDetails.objects.filter(student=user).select_related(
        "course"
    )

    context = {
        "courses_with_teachers": courses_with_teachers,
        "submissions": submissions,
    }
    return render(request, "StudentHome.html", context)


# show quiz for a particular course
@never_cache
def ShowQuiz(request, course_id):
    question_index = int(request.GET.get("question_index", 0))
    course = Courses.objects.get(id=course_id)
    questions = Quiz.objects.filter(course=course)

    # if there is no quiz
    if len(questions) == 0:
        return render(request, "Quiz.html", {"questions": "no_quiz"})

    # handling ajax request and saving in the session to get the total score
    if request.method == "POST":
        selected_answer = request.POST.get("answer")

        # Store the answer in the session

        quiz_answers = request.session.get("quiz_answers", {})
        quiz_answers[str(question_index + 1)] = selected_answer
        request.session["quiz_answers"] = quiz_answers
        return JsonResponse({"status": "success"})

        # Check if all questions are answered

    if question_index >= len(questions):

        # All answers submitted, calculate score

        print("insie of te loo")
        quiz_answers = request.session.get("quiz_answers", {})

        score = calculate_score(quiz_answers, questions)
        request.session.pop("quiz_answers", None)  # Clear session

        # Prepare context for results page
        total_questions = len(questions)
        email = request.session["email"]
        user = CustomUser.objects.get(email=email)
        current_date = timezone.now()
        print(current_date)
        QuizSubmissionDetails.objects.create(
            student=user, course=course, score=score, date=current_date
        )

        return render(
            request,
            "QuizResult.html",
            {"score": score, "total_questions": total_questions, "course": course},
        )

    current_question = questions[question_index]
    answer_options = [
        current_question.correct_answer
    ] + current_question.incorrect_answers
    random.shuffle(answer_options)

    return render(
        request,
        "Quiz.html",
        {
            "course": course,
            "current_question": current_question,
            "question_index": question_index,
            "total_questions": len(questions),
            "answer_options": answer_options,
        },
    )


# calcualting the score of the quiz
def calculate_score(answers, questions):
    score = 0
    print("answers", answers)
    for index, question in enumerate(questions):
        selected_answer = answers.get(str(index + 1))  # Convert index to string
        if selected_answer == question.correct_answer:
            score += 1
    return score
