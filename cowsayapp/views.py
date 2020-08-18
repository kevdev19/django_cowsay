from django.shortcuts import render


# Has a view for the index that does two things:
# 1) if there is output, render it to the browser
# 2) Always renders a fresh version of the form


def index_view(request):
    return render(request, 'index.html', {})
