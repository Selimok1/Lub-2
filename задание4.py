import re

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)

with open('emails.txt', 'w', encoding='utf-8') as f: # сохраняем почты в файл emails.txt
    for email in emails:
        f.write(email + '\n')

with open('phones.txt', 'w', encoding='utf-8') as f: # сохраняем номера телефонов в файл phones.txt
    for phone in phones:
        f.write(phone + '\n')

print("Почты и номера сохранены в отдельные файлы.")