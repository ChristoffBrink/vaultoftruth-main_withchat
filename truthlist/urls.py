from django.urls import path 
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('assessment/', views.assessment, name='assessment'),
    path('add_to_certificate/<int:id>/<str:value>/', views.add_to_certificate, name='add_to_certificate'),
    path('add-new-question/', views.add_new_question, name='add_new_question'),
    path('pending-questions/', views.pending_questions, name='pending_questions'),
    path('approve-question/<int:id>/', views.approve_question, name='approve_question'),
    path('reject-question/<int:id>/', views.reject_question, name='reject_question'),
    path('public-believes/', views.public_believes, name='public_believes'),
    path('reasons/<int:id>/', views.reasons, name='reasons'),
    path('debate/<int:id>/', views.debate, name='debate'),
    path('download-certificate/', views.download_certificate, name='download_certificate'),
    path('download-multiple-pdf/<int:range_start>/', views.download_multiple_pdf, name='download_multiple_pdf'),
    path('reasons-opinion/<int:id>/', views.reasons_opinion, name='reasons_opinion'),
    path('category', views.category, name='category'),
    path('category-question/<int:id>/', views.category_question, name='category_question'),
    path('add-comment/<int:id>/', views.add_comment, name='add_comment'),
    path('delete-comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('update-believes/<int:id>/', views.update_believes, name='update_believes'),
    path('add-reply/<int:id>/', views.add_reply, name='add_reply'),
    path('delete-reply/<int:id>/', views.delete_reply, name='delete_reply'),
    path('check-for-reply/<int:comment_id>/<int:reply_id>/', views.check_for_reply, name='check_for_reply'),
    
    path('like-comment/<int:id>/', views.like_comment, name='like_comment'),
    path('dislike-comment/<int:id>/', views.dislike_comment, name='dislike_comment'),
    path('remove-like-comment/<int:id>/', views.remove_like_comment, name='remove_like_comment'),
    path('remove-dislike-comment/<int:id>/', views.remove_dislike_comment, name='remove_dislike_comment'),
    path('like-reply/<int:id>/', views.like_reply, name='like_reply'),
    path('dislike-reply/<int:id>/', views.dislike_reply, name='dislike_reply'),
    path('remove-like-reply/<int:id>/', views.remove_like_reply, name='remove_like_reply'),
    path('remove-dislike-reply/<int:id>/', views.remove_dislike_reply, name='remove_dislike_reply'),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
