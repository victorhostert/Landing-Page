from django.shortcuts import render
from django.views.generic import ListView
from .models import Depoimento, Case

# Create your views here.
def LandingPageView(request):
    return render(request, 'index.html')

class CaseListView(ListView):
    model = Case
    template_name = 'cases_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depoimentos'] = Depoimento.objects.all()
        return context


# class PostsListView(CaseListView):
#     model = Post
#     template = 'post_list.html'