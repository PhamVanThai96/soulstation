from transformers import MarianMTModel, MarianTokenizer

# Câu tiếng Anh cần dịch
src_text = ["This is a sentence about electromagnetism."]

# Tải model MarianMT tiếng Anh → Việt
model_name = "Helsinki-NLP/opus-mt-en-vi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Mã hóa & dịch
inputs = tokenizer(src_text, return_tensors="pt", padding=True)
translated = model.generate(**inputs)
translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

print("→ Bản dịch:", translated_text[0])
