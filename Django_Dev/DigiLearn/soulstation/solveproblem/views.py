from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Question
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

import json
from bs4 import BeautifulSoup, NavigableString
from deep_translator import GoogleTranslator

CURRENT_QUEST_NUMDER = 32

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

def random_k_questions(k):
    total = Question.objects.count()
    k = min(k, total)
    question_list = Question.objects.order_by('?')[:k]
    original_question = get_question_by_number(CURRENT_QUEST_NUMDER)
    translated_question = extract_and_translate(original_question)

    global QUESTIONS
    QUESTIONS = [{
        'id' : 0,
        'original' : original_question,
        'translated' : translated_question, 
    }]
    # QUESTIONS = [{
    #     'id': q.question_id,
    #     'original': q.original_text,
    #     'translated': q.translated_text
    # } for q in question_list]
    return


def get_answer_by_number(number=8):
    url = "https://openstax.org/books/college-physics-ap-courses-2e/pages/chapter-34"
    response = requests.get(url)
    response.raise_for_status()
    
    # Đảm bảo đúng encoding để không bị lỗi ký tự
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lấy tất cả các div chứa lời giải
    solve_divs = soup.find_all('div', attrs={'data-type': 'solution'})

    count = 0

    for solve in solve_divs:
        count += 1
        number_tag = solve.find('a', class_='os-number')

        if number_tag and number_tag.text.strip().isdigit():
            if int(number_tag.text.strip()) == number:
                solution_html = str(solve_divs[count-1])
                return solution_html

    return f"⚠️ Không tìm thấy lời giải thứ {number}."

def get_question_by_number(number=8):
    url = 'https://openstax.org/books/college-physics-ap-courses-2e/pages/34-problems-exercises'
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả div có data-type="problem"
    problem_divs = soup.find_all('div', attrs={'data-type': 'problem'})

    if len(problem_divs) >= number:
        question_html = str(problem_divs[number - 1])  # vì list bắt đầu từ 0
        return question_html
    else:
        return "<p>Không tìm thấy câu hỏi yêu cầu.</p>"

def extract_and_translate(html_input):
    soup = BeautifulSoup(html_input, 'html.parser')
    
    # Duyệt tất cả phần tử con trong thẻ problem
    for element in soup.find_all(text=True):
        if isinstance(element, NavigableString):
            parent = element.parent

            # Bỏ qua nếu chỉ là khoảng trắng
            if element.strip():
                try:
                    translated = GoogleTranslator(source='en', target='vi').translate(text=element.strip())
                    element.replace_with(" " + translated + " ")
                except Exception as e:
                    print(f"Lỗi khi dịch: {e}")
    
    return str(soup)


def question_page(request):
    number_questions = 10
    random_k_questions(number_questions)

    return render(request, 'question_page.html', {'question': QUESTIONS[0]})

@csrf_exempt
def get_next_question(request):
    if request.method == 'POST':
        # current_id = int(request.POST.get('current_id', 1))
        # next_index = current_id % len(QUESTIONS)
        return JsonResponse(QUESTIONS[1])

@csrf_exempt
def get_previous_question(request):
    if request.method == 'POST':
        # current_id = int(request.POST.get('current_id', 1))
        # prev_index = (current_id - 2) % len(QUESTIONS)
        return JsonResponse(QUESTIONS[1])

@csrf_exempt
def get_answer_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_number = data.get('question_number')

        # Tùy ý xử lý logic câu trả lời
        answer = get_answer_by_number(CURRENT_QUEST_NUMDER)

        return JsonResponse({'answer_html': answer})

    return JsonResponse({'error': 'Invalid request'}, status=400)
