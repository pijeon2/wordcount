from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    find_YJ = 0
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word]=1
    for i in words:  #글에 '윤진'이 몇 번 들어가는지 세어주는 기능
        if '윤진' in i:
            num = i.count('윤진')
            find_YJ += num
        if i in word_dictionary:
            word_dictionary[i] +=1
        else:
            word_dictionary[i] = 1
    return render(request, 'result.html', {'full' : text, 'total' : len(words), 'dictionary' : word_dictionary.items(), 'find_YJ': find_YJ })