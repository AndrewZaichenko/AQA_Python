# Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters",
# наприклад "Word 'Python' has 6 letters". Для отримання слова для аналізу скористайтеся константою або функцією input().

user_word = input('Please enter a word to get info --> ').strip()
quantity_of_letters = len(user_word)
first_letter = user_word[0]
last_letter = user_word[-1]
word_info_1 = f"Word '{user_word.upper()}' has {quantity_of_letters} letters. It starts with letter '{first_letter.upper()}', and ends with letter '{last_letter.upper()}'."
print(word_info_1)
