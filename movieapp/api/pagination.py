from rest_framework.pagination import (PageNumberPagination, LimitOffsetPagination,
                                       CursorPagination)


class WatchListPagination(PageNumberPagination):
    page_size = 10

    # we can reaname the query param using below variable
    # page_query_param = 'p'

    # we can add page size query param
    # page_size_query_param = 'size'

    # we can restrict max size
    # max_page_size = 100

    # we can get last page try page=end
    # last_page_strings = "end"


class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = "limit"
    offset_query_param = "start"


class WatchListCursorPagination(CursorPagination):

    page_size = 5
    ordering = "created"   # field name you want to ordering
    cursor_query_param = "record"
