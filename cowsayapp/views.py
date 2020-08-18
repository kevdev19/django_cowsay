from django.shortcuts import render, HttpResponseRedirect, reverse

from cowsayapp.models import InputHistory
from .forms import InputForm


# Has a view for the index that does two things:
# 1) if there is output, render it to the browser
# 2) Always renders a fresh version of the form


def index_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            InputHistory.objects.create(
                capture_text=data.get('capture_text')
            )
            return HttpResponseRedirect(reverse("home"))

    form = InputForm()
    return render(request, 'index.html', {"form": form})
