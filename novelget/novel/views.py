from django.shortcuts import render_to_response
from django.http import HttpResponse, StreamingHttpResponse

# from .findbook import findbook
from .findbookinbaidu import findbook, getbook, downloadbook
# Create your views here.


def index(request):
    return render_to_response('novel/search.html')


def search(request):

    if 'bookname' in request.GET and request.GET['bookname']:
        bookname = request.GET['bookname']
        results = findbook(bookname)
        # results = findbookinbaidu(bookname)
        return render_to_response('novel/search_result.html', {'bookname': bookname, 'results': results})
    else:
        return HttpResponse('输入你想要搜的书名...')


def read(request, booknumber):
    # print(bookname, booknumber)
    chapter_list = getbook(booknumber)

    return render_to_response('novel/read_index.html', {'chapter_list': chapter_list})


def download(request, booknumber):

    file_name = 'xx.txt'
    response = StreamingHttpResponse(downloadbook(booknumber))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    return response
