from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    "it will define numbers of records in one page"
    page_size = 5
    "it will convert api page into p"
    # don't give : ?page=2  give : ?p=2
    page_query_param = 'p'
    "if you want to client define our page size so give :"
    # &records=10 : give this value to browser's api
    page_size_query_param = 'records'
    "it will redirect you to last page"
    last_page_strings = 'end'
