from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from .exception import RestException


class Paginator(object):
    """
    Rest paginator for list and querysets
    """

    def __init__(self, qs, request):
        self.qs = qs
        self.offset = self._get_offset(request)
        self.base = self._get_base(request)
        self.total = self._get_total()

    def _get_total(self):
        return self.qs.count()

    def _get_offset(self, request):
        offset = request.META.get('HTTP_X_OFFSET', '0')
        if offset.isdigit():
            return int(offset)
        else:
            raise RestException(_('X-Offset must be natural number'))

    def _get_base(self, request):
        base = request.META.get('HTTP_X_BASE')
        if not base:
            return None
        elif base.isdigit():
            return int(base)
        else:
            raise RestException(_('X-Base must be natural number or empty'))

    @property
    def page_qs(self):
        if self.base is not None:
            return self.qs[self.offset:(self.offset + self.base)]
        else:
            return self.qs[self.offset:]
