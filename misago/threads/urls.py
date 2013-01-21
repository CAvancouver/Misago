from django.conf.urls import patterns, url

urlpatterns = patterns('misago.threads.views',
    url(r'^forum/(?P<slug>(\w|-)+)-(?P<forum>\d+)/$', 'ThreadsView', name="forum"),
    url(r'^forum/(?P<slug>(\w|-)+)-(?P<forum>\d+)/(?P<page>\d+)/$', 'ThreadsView', name="forum"),
    url(r'^forum/(?P<slug>(\w|-)+)-(?P<forum>\d+)/new/$', 'PostingView', name="thread_new", kwargs={'mode': 'new_thread'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/$', 'ThreadView', name="thread"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/last/$', 'LastReplyView', name="thread_last"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/find-(?P<post>\d+)/$', 'FindReplyView', name="thread_find"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/new/$', 'NewReplyView', name="thread_new"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/moderated/$', 'FirstModeratedView', name="thread_moderated"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/reported/$', 'FirstReportedView', name="thread_reported"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<page>\d+)/$', 'ThreadView', name="thread"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/reply/$', 'PostingView', name="thread_reply", kwargs={'mode': 'new_post'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<quote>\d+)/reply/$', 'PostingView', name="thread_reply", kwargs={'mode': 'new_post'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/edit/$', 'PostingView', name="thread_edit", kwargs={'mode': 'edit_thread'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<post>\d+)/edit/$', 'PostingView', name="post_edit", kwargs={'mode': 'edit_post'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/delete/$', 'DeleteView', name="thread_delete", kwargs={'mode': 'delete_thread'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/hide/$', 'DeleteView', name="thread_hide", kwargs={'mode': 'hide_thread'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<post>\d+)/delete/$', 'DeleteView', name="post_delete", kwargs={'mode': 'delete_post'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<post>\d+)/hide/$', 'DeleteView', name="post_hide", kwargs={'mode': 'hide_post'}),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<post>\d+)/changelog/$', 'ChangelogView', name="changelog"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<post>\d+)/changelog/(?P<change>\d+)/$', 'ChangelogDiffView', name="changelog_diff"),
    url(r'^thread/(?P<slug>(\w|-)+)-(?P<thread>\d+)/(?P<post>\d+)/changelog/(?P<change>\d+)/revert/$', 'ChangelogRevertView', name="changelog_revert"),
)