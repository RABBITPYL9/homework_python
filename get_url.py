def get_absolute_url(url, *args, **kwargs):
    for i in args:
        url += '/' +i
        url += '?'
    for k, v in kwargs.items():
        url += '&' + k + '=' + v
        print(url)



get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin')
get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small')

#www.yandex.ru/posts/news?id=24&author=admin
#www.google.com/images?id=24&category=auto&color=red&size=small