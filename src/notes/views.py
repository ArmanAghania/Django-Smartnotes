from django.shortcuts import render
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from .forms import NotesForm
from django.views.generic import CreateView, DetailView ,ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()
    

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'notes'

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {
#         'notes': all_notes
#     })

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note Does Not Exist')
    
#     return render(request, 'notes/notes_detail.html', {
#         'note': note
#     })