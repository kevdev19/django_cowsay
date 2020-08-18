from django.shortcuts import render, HttpResponseRedirect, reverse

from cowsayapp.models import InputHistory
from .forms import InputForm

import subprocess

# Has a view for the index that does two things:
# 1) if there is output, render it to the browser
# 2) Always renders a fresh version of the form


def index_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cow_data = data.get('capture_text')
            InputHistory.objects.create(
                capture_text=data.get('capture_text')
            )

        cowsay_response = subprocess.run(
            ['cowsay', cow_data], capture_output=True, text=True)
        print(cowsay_response.stdout)
        return render(request, 'index.html', {"form": InputForm(), "cowsay_response": cowsay_response.stdout})

    form = InputForm()
    return render(request, 'index.html', {"form": form})


def history_view(request):
    # Received help from Sohail Aslam on this line
    # This line filters the output ordering by negative id field
    # and only showing up to 10 items from the capture_text field
    history = InputHistory.objects.filter().order_by('-id')[:10]
    return render(request, 'history.html', {"history": history})
