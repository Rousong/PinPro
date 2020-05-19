from __future__ import unicode_literals

from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = "核心"

    # signals are imported, so that they are defined and can be used
    def ready(self):
        import core.signals