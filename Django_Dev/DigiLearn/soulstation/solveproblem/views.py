from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def members(request):
    template = loader.get_template('question_page.html')
    return HttpResponse(template.render())

QUESTIONS = [
    {
        'id': 1,
        'original': "What is the speed of light in a vacuum?",
        'translated': "Tốc độ ánh sáng trong chân không là bao nhiêu?"
    },
    {
        'id': 2,
        'original': "What is the Planck constant?",
        'translated': "Hằng số Planck là gì?"
    },
    {
        'id': 3,
        'original': "Explain the uncertainty principle.",
        'translated': "Giải thích nguyên lý bất định."
    },
]

# def show_question(request):
#     # Ví dụ dữ liệu câu hỏi từ database hoặc tạm thời
#     question_data = {
#         'id': 28,
#         'original': "Assume the average density of the universe is 0.1 of the critical density needed for closure. What is the average number of protons per cubic meter, assuming the universe is composed mostly of hydrogen?",
#         'translated': "Giả sử mật độ trung bình của vũ trụ là 0,1 mật độ tới hạn cần thiết để đóng. Số lượng proton trung bình trên mỗi mét khối là bao nhiêu, giả sử vũ trụ được cấu tạo chủ yếu là hydro là bao nhiêu?"
#     }

#     return render(request, 'question_page.html', {'question': question_data})


def question_page(request):
    return render(request, 'question_page.html', {'question': QUESTIONS[0]})

@csrf_exempt
def get_next_question(request):
    if request.method == 'POST':
        current_id = int(request.POST.get('current_id', 1))
        next_index = current_id % len(QUESTIONS)
        return JsonResponse(QUESTIONS[next_index])

@csrf_exempt
def get_previous_question(request):
    if request.method == 'POST':
        current_id = int(request.POST.get('current_id', 1))
        prev_index = (current_id - 2) % len(QUESTIONS)
        return JsonResponse(QUESTIONS[prev_index])

