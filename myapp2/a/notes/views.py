from django.shortcuts import render


# Home View
def home(request):
    return render(request, "home.html")

# Test page
def test(request):
    return render(request, "test.html")

# Notes page
def notes(request):
    return render(request, "notes.html")

def page1(request):
    title = "Sample Text"
    body = 'This is some sample text to show on a page.'
    data = {'title': title, 'body': body}
    return render(request, "page.html", data)

