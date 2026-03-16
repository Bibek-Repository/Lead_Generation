from django.shortcuts import render, redirect
from .forms import LeadForm

def capture_lead(request):

    if request.method == "POST":
        form = LeadForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = LeadForm()

    return render(request, 'lead_form.html', {'form': form})


def success(request):
    return render(request, 'success.html')