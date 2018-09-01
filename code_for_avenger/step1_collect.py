#http://www.demodashi.com/demo/13257.html

from urllib import request

from bs4 import BeautifulSoup as bs

for i in range(0, 11):
    # res = request.urlopen('https://movie.douban.com/subject/24773958/comments?start=' + str(
    #     20 * i) + '&limit=20&sort=new_score&status=P&percent_type=')

    res = request.urlopen('https://movie.douban.com/subject/2133323/comments?start=' + str(
        20 * i) + '&limit=20&sort=new_score&status=P&percent_type=')

    #  https://book.douban.com/subject/5948760/comments/
    #res = request.urlopen('https://book.douban.com/subject/5948760/comments/hot?p=' + str(i))
    html_data = res.read().decode('utf-8')

    Soup = bs(html_data, 'html.parser')
    comments = Soup.find_all('div', id='comments')
    #print(type(comments))
    #print(comments[0])
    comments_content = comments[0].find_all('p')
    print(type(comments_content))
    for j in range(0, 20):
        #print(len(comments_content))
        text = str(comments_content[j])
        f = open('movie_comments.txt', 'a', encoding='utf-8')
        f.write(text)
        f.close()

