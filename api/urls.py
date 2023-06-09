from django.urls import path
from .views import authentification, user, administrator, moderator


urlpatterns = [
    path('auth/signin', authentification.signin_view),
    path('auth/login', authentification.login_view),
    path('auth/logout', authentification.logout_view),
    path('user/feedback', user.feedback_view),
    path('user/timetables/followed', user.get_timetable_follow_by_me_view),
    path('user/timetable/<int:timetable_pk>/follow/<str:timetable_code>', user.follow_timetable_view),
    path('user/timetable/<int:timetable_pk>/unfollow', user.unfollow_timetable_view),
    path('user/timetables', user.get_timetable_view),
    path('user/status/choices', user.get_status_choice_view),
    path('user/timetable/<int:timetable_pk>/classes', user.get_timetable_classes_view),
    path('user/timetable/<int:timetable_pk>/classes/<int:next_day>', user.get_timetable_classes_view),
    path('user/timetable/<int:timetable_pk>/lecturers', user.get_timetable_lecturer_view),
    path('user/timetable/<int:timetable_pk>/locations', user.get_timetable_location_view),
    path('user/timetable/<int:timetable_pk>/courses', user.get_timetable_course_view),
    path('user/timetable/<int:timetable_pk>/categories', user.get_timetable_category_view),
    path('user/timetable/<int:timetable_pk>/events', user.get_timetable_event_view),
    path('user/timetable/<int:timetable_pk>/events/<int:next_day>', user.get_timetable_event_view),
    path('user/timetable/<int:timetable_pk>/assets', user.get_timetable_asset_view),
    path('user/timetable/asset/<asset_pk>/read', user.set_asset_reader_view),
    path('user/timetable/media/<media_pk>/download', user.download_media_view),
    path('user/timetable/notifications', user.get_notification),
    path('user/timetable/announces', user.get_announce),
    path('admin/feedback/read', administrator.get_feedback_view),
    path('admin/timetable/add', administrator.add_timetable_view),
    path('admin/timetable/<int:timetable_pk>/update', administrator.update_timetable_view),
    path('admin/timetable/<int:timetable_pk>/delete', administrator.delete_timetable_view),
    path('admin/timetable/<int:timetable_pk>/moderator/add/<int:user_pk>', administrator.add_timetable_moderator_view),
    path('admin/timetable/<int:timetable_pk>/moderator/remove/<int:user_pk>', administrator.remove_timetable_moderator_view),
    path('admin/timetable/course/add', administrator.add_timetable_course_view),
    path('admin/timetable/course/<int:course_pk>/update', administrator.add_timetable_course_view),
    path('admin/timetable/course/<int:course_pk>/delete', administrator.add_timetable_course_view),
    path('admin/timetable/<int:timetable_pk>/followers', administrator.get_timetable_follower_view),
    path('admin/timetable/<int:timetable_pk>/lecturer/add', administrator.add_timetable_lecturer_view),
    path('admin/timetable/lecturer/<int:lecturer_pk>/update', administrator.update_timetable_lecturer_view),
    path('admin/timetable/lecturer/<int:lecturer_pk>/delete', administrator.delete_timetable_lecturer_view),
    path('admin/timetable/<int:timetable_pk>/location/add', administrator.add_timetable_location_view),
    path('admin/timetable/location/<int:location_pk>/update', administrator.update_timetable_location_view),
    path('admin/timetable/location/<int:location_pk>/delete', administrator.delete_timetable_location_view),
    path('admin/timetable/<int:timetable_pk>/category/add', administrator.add_timetable_category_view),
    path('admin/timetable/category/<int:category_pk>/update', administrator.update_timetable_category_view),
    path('admin/timetable/category/<int:category_pk>/delete', administrator.delete_timetable_category_view),
    path('moderator/media/add', moderator.add_media_view),
    path('moderator/timetable/course/<int:course_pk>/classe/add', moderator.add_timetable_classe_view),
    path('moderator/timetable/classe/<int:classe_pk>/update', moderator.update_timetable_classe_view),
    path('moderator/timetable/classe/<int:classe_pk>/delete', moderator.delete_timetable_classe_view),
    path('moderator/timetable/classe/<int:classe_pk>/status/<str:status>', moderator.update_status_timetable_classe_view),
    path('moderator/timetable/classe/<int:classe_pk>/attend/toggle', moderator.update_attend_timetable_classe_view),
    path('moderator/timetable/course/<int:course_pk>/asset/add', moderator.add_course_asset_view),
    path('moderator/timetable/asset/<int:asset_pk>/update', moderator.update_course_asset_view),
    path('moderator/timetable/asset/<int:asset_pk>/delete', moderator.delete_course_asset_view),
    path('moderator/timetable/event/add', moderator.add_timetable_event_view),
    path('moderator/timetable/event/<int:event_pk>/update', moderator.update_timetable_event_view),
    path('moderator/timetable/event/<int:event_pk>/delete', moderator.delete_timetable_event_view),
]
