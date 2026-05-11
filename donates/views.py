from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

def update_donate_view(request,id):
    donate_id = get_object_or_404(models.Donate, id=id)
    if request.method == 'POST':
        form = forms.DonateForm(request.POST, instance=donate_id)
        if form.is_valid():
            form.save()
            return redirect('/donate_list/')
    else:
        form = forms.DonateForm(instance=donate_id)
    return render(request, 'donates/update_donate.html', {
        "form": form,
        'donate_id': donate_id,
    })





def delete_donate_view(request, id):
    donate_id = get_object_or_404(models.Donate, id=id)
    donate_id.delete()
    return redirect('/donate_list/')




def create_donate_view(request):
    if request.method == "POST":
        form = forms.DonateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/donate_list/')
    else:
        form = forms.DonateForm()
    return render(request, 'donates/create_donate.html', {'form': form})


def donate_list_view(request):
    if request.method == "GET":
        donate = models.Donate.objects.all().order_by('-id')
    return render(request, 'donates/donate_list.html', {'donate': donate})
    

    