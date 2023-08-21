import validators

def validBooru(link, legal):
    for i in legal:
        if link[:i[0]] == i[1]:
            return True
    return False

path = r"C:\Users\papas\Desktop\links.txt"
with open(path) as links:
    urls = []
    table = str.maketrans({"\n":"", "\"":"", " ":"", ",":""})
    allowed = [(49,"https://rule34.xxx/index.php?page=post&s=view&id="),
               (27,"https://e621.net/post/show/"),
               (49,"https://xbooru.com/index.php?page=post&s=view&id="),
               (51,"https://gelbooru.com/index.php?page=post&s=view&id="),
               (29,"https://atfbooru.ninja/posts/"),
               (52,"https://safebooru.org/index.php?page=post&s=view&id="),
               (33,"https://danbooru.donmai.us/posts/")]
    
    for line in links.readlines():
        line = line.translate(table)
        if validBooru(line,allowed):
            urls.append(line)
    
    for link in urls:
        print(link)
