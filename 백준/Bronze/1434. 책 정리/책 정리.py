N,M=map(int,input().split())
waste=0
box_list=list(map(int,input().split()))
book_list=list(map(int,input().split()))
while (len(book_list)!=0):
    if(box_list[0] >= book_list[0]):
        box_list[0]-=book_list[0]
        book_list.pop(0)
    else:
        waste+=box_list[0]
        box_list.pop(0)
print(waste+sum(box_list))