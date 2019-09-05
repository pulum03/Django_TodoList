from django.shortcuts import render
from .models import TodoList
from django.views import generic
from todo_board.form import TodoForm

# Create your views here.
class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_board_list.html'
        todo_list = TodoList.objects.all() #  모든 객체를 가져옵니다
        return render(request, template_name, {"todo_list" : todo_list}) # 그리고 그 결과 값을 {"todo_list": todo_list} 에 담아서 이제 template으로 넘겨줍니다~
    
class Todo_board_detail(generic.DetailView):
    model = TodoList
    template_name = 'todo_board/todo_board_detail.html'
    context_object_name = 'todo_list'

class Todo_board_update(generic.UpdateView):
    model = TodoList
    fields = ('title', 'content', 'end_date')
    template_name = 'todo_board/todo_board_update.html'
    success_url = '/board/'
    
    def form_valid(self, form):
        form.save()
        return render(self.request, 'todo_board/todo_board_success.html', {"message" : "list up-to-dated"})

    def get(self, request, *args, **kwargs):
        # 오블젝트를 받아서 폼 클래스를 받은 후 이것을 return 해줘야됨
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        
        return self.render_to_response(context) 

class Todo_board_delete(generic.DeleteView):
    model = TodoList
    success_url = '/board/'
    context_object_name = 'todo_list'
    
def check_post(request):
    template_name = 'todo_board/todo_board_success.html'
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit = False)
            todo.todo_save()
            message = "일정 추가"
            return render(request, template_name, {"message" : message})
    else:
        template_name = 'todo_board/todo_board_insert.html'
        form = TodoForm
        return render(request, template_name, {"form" : form})