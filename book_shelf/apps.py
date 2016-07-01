from __future__ import unicode_literals

from django.apps import AppConfig


class BookShelfConfig(AppConfig):
    name = 'book_shelf'
    verbose_name = 'Bookshelf App'

    def ready(self):
        import book_shelf.signals
