from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    def __init__(self):
        self.request = None

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

    def paginate_queryset(self, queryset, request, view=None):
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 10))
        self.request = request
        self.limit = limit
        self.offset = offset
        self.count_all = self.get_count(queryset)
        queryset = queryset[offset:offset + limit]
        self.count = self.get_count(queryset)

        return list(queryset)

    def get_next_link(self):
        if self.offset + self.limit >= self.count_all:
            return ''
        next_offset = self.offset + self.limit

        return self.request.build_absolute_uri(f"?limit={self.limit}&offset={next_offset}")

    def get_previous_link(self):
        if self.offset <= 0:
            return None
        previous_offset = max(0, self.offset - self.limit)

        return self.request.build_absolute_uri(f"?limit={self.limit}&offset={previous_offset}")
