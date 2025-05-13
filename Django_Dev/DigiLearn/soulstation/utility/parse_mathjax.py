import requests
from bs4 import BeautifulSoup
import json

# Lấy trang HTML
url = 'https://openstax.org/books/college-physics-ap-courses-2e/pages/34-problems-exercises'
response = requests.get(url)
response.raise_for_status()

# Phân tích nội dung
soup = BeautifulSoup(response.text, 'html.parser')

# Tìm tất cả các câu hỏi (có thể cần sửa selector tùy trang)
questions = soup.find_all('div', {'data-type': 'problem'})

def extract_question_with_mathjax(element):
    parts = []
    for content in element.contents:
        if content.name == 'span' and 'MathJax_Preview' in content.get('class', []):
            # Nội dung công thức
            parts.append(f"\\({content.get_text(strip=True)}\\)")
        elif content.name:
            parts.append(content.get_text(strip=True))
        else:
            parts.append(content.strip())
    return ' '.join(parts)

# Lấy câu hỏi số 8 (index 7 vì bắt đầu từ 0)
if len(questions) >= 8:
    question_text = extract_question_with_mathjax(questions[7])
    output = {
        "question_number": 8,
        "content": question_text
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
else:
    print(json.dumps({"error": "Không tìm thấy đủ câu hỏi."}, ensure_ascii=False))
