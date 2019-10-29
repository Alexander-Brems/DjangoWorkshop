from django.shortcuts import render


# Home View
def home(request):
    title = "App 2c - View Inheritance - Home Page"
    text = '<p>Body Text is injected into the page template.</p>'
    link = '<a href="test">Test page</a>'
    content = '<h2>Home Page</h2>'
    data = dict(title=title, content=content + link + text)
    return render(request, "home.html", data)


# Test page
def test(request):
    title = "App 2c - View Inheritance - Test Page"
    content = '<h2>Test Page</h2><p>Body Text is injected into the page template.</p>'
    data = dict(title=title, content=content)
    return render(request, "test.html", data)


# Notes page
def notes(request):
    title = "App 2c - View Inheritance - Notes Page"
    note = 'This information is passed from the view into the "notes.html" template.'
    data = dict(title=title, note=note)
    return render(request, "notes.html", data)


# Missing page
def missing(request):
    title="Page Not Found"
    data = dict(title=title, url=request.path) 
    return render(request, "missing.html", data)


# UNC View
def unc(request):
    title = "App 2c - View Inheritance - UNC Page"
    return render(request, "unc.html", dict(title=title))
