from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def start(request):
    return render(request, 'start.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    length = len(text)
    no_enter = (len([i for i in text if i != '\n']))

    for leng in text:
        if leng in " " :
            length -= 1
        elif leng in "\n":
            length -= 2

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total': len(words),
    'dictionary': word_dictionary.items(), 'no_enter': no_enter, 'no_space': length})