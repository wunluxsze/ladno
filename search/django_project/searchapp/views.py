from django.shortcuts import render
from searchapp import func

def search_sentence(request): #функция для отправки списка в html
    search_check = False
    if 'q' in request.GET and request.GET["q"] != '':
        search_check = True
        result = func.search_sentence(request.GET["q"], "words.txt") #отправка слова которое нужно найти и файла с текстом
        return render(request, 'index.html', context={"sentences": result, 'check': search_check}) #отправка списка и переменную которая проверяет есть ли запрос
    return render(request, 'index.html')  #если пустое то обновляется страница


