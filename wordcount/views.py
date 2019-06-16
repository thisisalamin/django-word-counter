from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'index.html')


def count(request):
    wordlist = request.POST['fulltext']
    textcount = wordlist.split()
    return render(request, 'count.html', {'fulltext': len(textcount)})
