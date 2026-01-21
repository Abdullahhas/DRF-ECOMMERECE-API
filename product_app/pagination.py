from rest_framework.pagination import CursorPagination

class MyPagination(CursorPagination):
    page_size = 3
    ordering = 'id'
    