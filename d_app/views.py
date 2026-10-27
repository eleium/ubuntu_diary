from django.shortcuts import get_object_or_404, render, redirect
from .models import Diary, Entry
from .forms import DiaryForm, EntryForm

# Create your views here.


def index(request):
    return render(request, "d_app/index.html")


def diaries(request):

    diaries = Diary.objects.order_by("date_added")
    context = {"diaries": diaries}
    return render(request, "d_app/diaries.html", context)


def diary(request, diary_id):
    # diary = Diary.objects.get(id=diary_id)
    # 使用get_object_or_404模式，如果输入不存在的id，比如888，直接转向404,而不是抛出异常DoseNotExit而崩溃。
    diary = get_object_or_404(Diary, id=diary_id)
    entries = diary.entry_set.order_by("-date_added")
    # return redirect('d_app:diaries')

    context = {"diary": diary, "entries": entries}
    return render(request, "d_app/diary.html", context)


def new_diary(request):

    if request.method != "POST":
        form = DiaryForm()

    else:
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            # 拿到new_diary的id.  在form.save()里面，有id,有text，有date_added等信息。
            new_diary = form.save()
            # 用拿到的new_diary的id,赋值给diary_id.重定向：页面跳到新建的这个日记分类里。所以diary_di=new_diary.id
            return redirect("d_app:diary,diary_id=new_diary.id")

    context = {"form": form}
    return render(request, "d_app/new_diary.html", context)


def edit_diary(request, diary_id):
    # diary = Diary.objects.get(id=diary_id) 用保险优雅的写法：
    diary = get_object_or_404(Diary, id=diary_id)

    if request.method != "POST":
        form = DiaryForm(instance=diary)
    else:
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect("d_app:diary", diary_id=diary.id)

    context = {"diary": diary, "form": form}
    return render(request, "d_app/edit_diary.html", context)


def del_diary(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)

    if request.method == "POST":
        diary.delete()
        return redirect("d_app:diaries")

    context = {"diary": diary}
    return render(request, "d_app/del_diary.html", context)
