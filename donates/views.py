from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

from django.views import generic

from django.urls import reverse



class UpdateDonateView(generic.UpdateView):
    template_name = 'donates/update_donate.html'
    form_class = forms.DonateForm
    model = models.Donate

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateDonateView, self).form_valid(form=form)
    
    def get_object(self, **kwargs):
        donate_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=donate_id)
    
    def get_success_url(self):
        return reverse('dt_list')






# def update_donate_view(request,id):
#     donate_id = get_object_or_404(models.Donate, id=id)
#     if request.method == 'POST':
#         form = forms.DonateForm(request.POST, instance=donate_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/donate_list/')
#     else:
#         form = forms.DonateForm(instance=donate_id)
#     return render(request, 'donates/update_donate.html', {
#         "form": form,
#         'donate_id': donate_id,
#     })





class DeleteDonateView(generic.DeleteView):
    template_name = 'donates/confirm_delete.html'
    model = models.Donate
    context_object_name = 'donate_id'

    def get_object(self, **kwargs):
        donate_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=donate_id)
    
    def get_success_url(self):
        return reverse('dt_list')
    




# def delete_donate_view(request, id):
#     donate_id = get_object_or_404(models.Donate, id=id)
#     donate_id.delete()
#     return redirect('/donate_list/')







class CreateDonateView(generic.CreateView):
    template_name = 'donates/create_donate.html'
    form_class = forms.DonateForm
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateDonateView, self).form_valid(form=form)
    
    def get_success_url(self):
        return reverse('dt_list')





# def create_donate_view(request):
#     if request.method == "POST":
#         form = forms.DonateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/donate_list/')
#     else:
#         form = forms.DonateForm()
#     return render(request, 'donates/create_donate.html', {'form': form})





class DonateListView(generic.ListView):
    template_name = 'donates/donate_list.html'
    context_object_name = 'donate'
    model = models.Donate
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')




# def donate_list_view(request):
#     if request.method == "GET":
#         donate = models.Donate.objects.all().order_by('-id')
#     return render(request, 'donates/donate_list.html', {'donate': donate})
    

