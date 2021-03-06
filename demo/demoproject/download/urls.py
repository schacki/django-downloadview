# coding=utf8
"""URL mapping."""
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'demoproject.download.views',
    # Model-based downloads.
    url(r'^document/(?P<slug>[a-zA-Z0-9_-]+)/$',
        'download_document',
        name='document'),
    # Storage-based downloads.
    url(r'^storage/(?P<path>[a-zA-Z0-9_-]+\.[a-zA-Z0-9]{1,4})$',
        'download_fixture_from_storage',
        name='fixture_from_storage'),
    # Path-based downloads.
    url(r'^hello-world\.txt$',
        'download_hello_world',
        name='hello_world'),
    url(r'^hello-world-inline\.txt$',
        'download_hello_world_inline',
        name='hello_world_inline'),
    url(r'^path/(?P<path>[a-zA-Z0-9_-]+\.[a-zA-Z0-9]{1,4})$',
        'download_fixture_from_path',
        name='fixture_from_path'),
    # URL-based downloads.
    url(r'^http/readme\.txt$',
        'download_http_hello_world',
        name='http_hello_world'),
    # Generated downloads.
    url(r'^generated/hello-world\.txt$',
        'download_generated_hello_world',
        name='generated_hello_world'),
)
