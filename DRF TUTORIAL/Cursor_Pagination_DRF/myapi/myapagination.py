from rest_framework.pagination import CursorPagination

# if you want to see by date then you want to implement a field in which  give value of datetime


class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'roll'
