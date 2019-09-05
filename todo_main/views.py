from django.shortcuts import render
from django.views import generic

# Create your views here.

class Todo_main(generic.TemplateView):
    # django : function based view, generic view
    # function based view : 사용자 세세한 코딩 가능
    # generic view : 간편하고 코드 단순
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/index.html'
        return render(request, template_name)

    # Todo_main에서 TemplateView(일반적인 view)를 보여주지만
    # get 방식으로 받을시, todo_main/index.html로 이동