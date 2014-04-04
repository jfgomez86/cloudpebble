from django.conf.urls import patterns, url

from ide.api import proxy_keen, check_task, get_shortlink
from ide.api.git import github_push, github_pull, set_project_repo, create_project_repo
from ide.api.phone import ping_phone, check_phone, list_phones, update_phone
from ide.api.project import project_info, compile_project, last_build, build_history, build_log, create_project, \
    save_project_settings, delete_project, begin_export, import_zip, import_github, do_import_gist
from ide.api.resource import create_resource, resource_info, delete_resource, update_resource, show_resource
from ide.api.source import create_source_file, load_source_file, source_file_is_safe, save_source_file, \
    delete_source_file
from ide.api.user import transition_accept, transition_export, transition_delete, whats_new
from ide.views.index import index
from ide.views.project import view_project, github_hook, build_status, import_gist
from ide.views.settings import settings_page, start_github_auth, remove_github_auth, complete_github_auth

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^project/create', create_project, name='create_project'),
    url(r'^project/(?P<project_id>\d+)$', view_project, name='project'),
    url(r'^project/(?P<project_id>\d+)/info', project_info, name='project_info'),
    url(r'^project/(?P<project_id>\d+)/save_settings', save_project_settings, name='save_project_settings'),
    url(r'^project/(?P<project_id>\d+)/delete', delete_project, name='delete_project'),
    url(r'^project/(?P<project_id>\d+)/create_source_file', create_source_file, name='create_source_file'),
    url(r'^project/(?P<project_id>\d+)/source/(?P<file_id>\d+)/load', load_source_file, name='load_source_file'),
    url(r'^project/(?P<project_id>\d+)/source/(?P<file_id>\d+)/save', save_source_file, name='save_source_file'),
    url(r'^project/(?P<project_id>\d+)/source/(?P<file_id>\d+)/is_safe', source_file_is_safe, name='source_file_is_safe'),
    url(r'^project/(?P<project_id>\d+)/source/(?P<file_id>\d+)/delete', delete_source_file, name='delete_source_file'),
    url(r'^project/(?P<project_id>\d+)/create_resource', create_resource, name='create_resource'),
    url(r'^project/(?P<project_id>\d+)/resource/(?P<resource_id>\d+)/info', resource_info, name='resource_info'),
    url(r'^project/(?P<project_id>\d+)/resource/(?P<resource_id>\d+)/delete', delete_resource, name='delete_resource'),
    url(r'^project/(?P<project_id>\d+)/resource/(?P<resource_id>\d+)/update', update_resource, name='update_resource'),
    url(r'^project/(?P<project_id>\d+)/resource/(?P<resource_id>\d+)/get', show_resource, name='show_resource'),
    url(r'^project/(?P<project_id>\d+)/build/run', compile_project, name='compile_project'),
    url(r'^project/(?P<project_id>\d+)/build/last', last_build, name='get_last_build'),
    url(r'^project/(?P<project_id>\d+)/build/history', build_history, name='get_build_history'),
    url(r'^project/(?P<project_id>\d+)/analytics', proxy_keen, name='proxy_analytics'),
    url(r'^project/(?P<project_id>\d+)/build/(?P<build_id>\d+)/log', build_log, name='get_build_log'),
    url(r'^project/(?P<project_id>\d+)/export', begin_export, name='begin_export'),
    url(r'^project/(?P<project_id>\d+)/github/repo$', set_project_repo, name='set_project_repo'),
    url(r'^project/(?P<project_id>\d+)/github/repo/create$', create_project_repo, name='create_project_repo'),
    url(r'^project/(?P<project_id>\d+)/github/commit$', github_push, name='github_push'),
    url(r'^project/(?P<project_id>\d+)/github/pull$', github_pull, name='github_pull'),
    url(r'^project/(?P<project_id>\d+)/github/push_hook$', github_hook, name='github_hook'),
    url(r'^project/(?P<project_id>\d+)/status\.png$', build_status, name='build_status'),
    url(r'^task/(?P<task_id>[0-9a-f-]{32,36})', check_task, name='check_task'),
    url(r'^shortlink$', get_shortlink, name='get_shortlink'),
    url(r'^settings$', settings_page, name='settings'),
    url(r'^settings/github/start$', start_github_auth, name='start_github_auth'),
    url(r'^settings/github/callback$', complete_github_auth, name='complete_github_auth'),
    url(r'^settings/github/unlink$', remove_github_auth, name='remove_github_auth'),
    url(r'^import/zip', import_zip, name='import_zip'),
    url(r'^import/github', import_github, name='import_github'),
    url(r'^import/gist', do_import_gist, name='import_gist'),
    url(r'^transition/accept', transition_accept, name='transition_accept'),
    url(r'^transition/export', transition_export, name='transition_export'),
    url(r'^transition/delete', transition_delete, name='transition_delete'),
    url(r'^ping_phone$', ping_phone),
    url(r'^check_phone/(?P<request_id>[0-9a-f-]+)$', check_phone),
    url(r'^update_phone$', update_phone),
    url(r'^list_phones$', list_phones),
    url(r'^whats_new', whats_new, name='whats_new'),
    url(r'^gist/(?P<gist_id>[0-9a-f]+)$', import_gist)
)
