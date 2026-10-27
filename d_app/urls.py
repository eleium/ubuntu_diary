from django.urls import path
from . import views


app_name = "d_app"

urlpatterns = [
    # 首页和列表
    path("", views.index, name="index"),
    path("diaries/", views.diaries, name="diaries"),
    # 日记种类名称的增删改查
    path("diary/<int:diary_id>/", views.diary, name="diary"),
    path("new_diary/", views.new_diary, name="new_diary"),
    path("edit_diary/<int:diary_id>/", views.edit_diary, name="edit_diary"),
    path("del_diary/<int:diary_id>/", views.del_diary, name="del_diary"),
    # 日记正文的增删改查,用嵌套的方式，一目了然
    path("diary/<int:diary_id>/entry/<int:entry_id>/", views.entry, name="entry"),
    path(
        "diary/<int:diary_id>/new_entry/",
        views.new_entry,
        name="new_entry",
    ),
    path(
        "diary/<int:diary_id>/edit_entry/<int:entry_id>/",
        views.edit_entry,
        name="edit_entry",
    ),
    path(
        "diary/<int:diary_id>/del_entry/<int:entry_id>/",
        views.del_entry,
        name="del_entry",
    ),
]
