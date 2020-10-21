import pathlib
print(pathlib.Path)
class FolderIterator:
    def __init__(self, foldername='base'):
        self.foldername = pathlib.Path(foldername)
fi = FolderIterator()
print(type(fi.foldername))
print(isinstance(fi.foldername, pathlib.Path))
# p=pathlib.Path('.')
# base_path=p / 'base' 
# uniqe=[]
# val=[]
# for fname in base_path.rglob("*"):
#      if fname.is_file():
#          f = open(fname, 'r')
#          n=f.read()
#          if not n in val:
#              val.append(n)
#              uniqe.append(fname.name)
#              uniqe.append(n)
#          f.close()
# print(uniqe)
# fkey=uniqe[0:len(uniqe):2]
# fval=uniqe[1:len(uniqe):2]
# dup={}
# i=0
# for x in fkey:
#     dup[x]=[]
#     v=fval[i]
#     for fname in base_path.rglob("*"):
#         if fname.is_file():
#             if fname.name!=x:
#                 f = open(fname, 'r')
#                 n=f.read()
#                 if n==v:
#                     dup[x].append(fname.name)
#     i=i+1
# print(dup)