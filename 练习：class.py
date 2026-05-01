class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
    def info(self):
        return f"《{self.name}》  作者：{self.author}"

    def is_long(self):
        if len(self.name) > 5:
            return "长标题"
        else:
            return "短标题"


book1 = Book("三体","刘慈欣")
book2 = Book("活着","余华")
book3 = Book("Python从入门到实践","Eric Matthes")
print(book1.info(),book1.is_long(),"\n",book2.info(),book2.is_long(),"\n",book3.info(),book3.is_long())