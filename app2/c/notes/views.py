from django.shortcuts import render


# Home View
def home(request):
    title = "App 2b - Variable Insertion - Home"
    body = 'Body Text'
    data = {'title': title, 'body': body}
    return render(request, "home.html", data)


# Test page
def test(request):
    title = "App 2b - Variable Insertion - Test"
    html = '''
        <p>
            This is simple Django app that was created using the default command script.
        </p>
        <p>
            This page uses HTML text from a template file "notes/templates/test.html".
        </p>
        <ul>
            <li>
                <a href="/">Visit Home</a>
            </li>
            <li>
                <a href="notes">Visit Notes</a>
            </li>
            <li>
                <a href="test">Visit Test</a>
            </li>
            <li>
                <a href="random">Visit Random Page</a>
            </li>
        </ul>
        '''
    data = {'title': title, 'body': html}
    return render(request, "test.html", data)


# Notes page
def notes(request):
    title = "App 2b - Variable Insertion - Notes"
    notes_body = '''
        <p>
            This is simple Django app that was created using the default command script.
        </p>
        <p>
            This page uses HTML text from a template file "notes/templates/test.html".
        </p>
        <ul>
            <li>
                <a href="/">Visit Home</a>
            </li>
            <li>
                <a href="notes">Visit Notes</a>
            </li>
            <li>
                <a href="test">Visit Test</a>
            </li>
            <li>
                <a href="random">Visit Random Page</a>
            </li>
        </ul>
        '''
    data = {'title': title, 'body': notes_body}
    return render(request, "notes.html", data)

