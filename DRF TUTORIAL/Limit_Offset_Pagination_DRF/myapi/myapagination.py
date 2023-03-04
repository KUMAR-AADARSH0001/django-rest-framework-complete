from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    # ?limit=4
    "give this into browser's api for get number of records"

    # &offset=9
    "for starting the number of list from 9"

    # pass

    default_limit = 5

    # ?limit=4  :  ?mylimit=4
    "if want to change limit into mylimit"
    limit_query_param = 'mylimit'

    # &offset=9  :  &myoffset=9
    "if want to change offset into myoffset"
    offset_query_param = 'myoffset'

    # &mylimit=anything=123
    "if you give limit 7 and more then 7 it will give only 6th page"
    max_limit = 6
