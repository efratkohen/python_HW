import pathlib
class FolderIterator:
    """.Iterates through the supplied folder, finding duplicates.

    Call the iter_folder() method to parse the directory.

    Attributes
    ----------
    foldername : path-like
        Name of base folder to iterate on.
    uniques : list
        A list of unique files in the folder and their content.
    duplicates : dict
        The keys are the parent files and the values are a list of filenames
        with the same content.
    """
    def __init__(self, foldername='base'):
        self.foldername = pathlib.Path(foldername)
        self.uniques = self.unique()
        self.duplicates = self.duplicate()


    def iter_folder(self):
        """Main function to find duplicate and unique files in the filesystem."""

        pass
    def unique (self):
            p=pathlib.Path('.')
            base_path=p / self.foldername 
            uniq=[]
            val=[]
            for fname in base_path.rglob("*"):
                if fname.is_file():
                    f = open(fname, 'r')
                    n=f.read()
                    if not n in val:
                        val.append(n)
                        uniq.append(fname.name)
                        uniq.append(n)
                    f.close()
            return uniq

    def duplicate (self):
        p=pathlib.Path('.')
        base_path=p / self.foldername
        uniq=self.unique()
        fkey=uniq[0:len(uniq):2]
        fval=uniq[1:len(uniq):2]
        dup={}
        i=0
        for x in fkey:
            dup[x]=[]
            v=fval[i]
            for fname in base_path.rglob("*"):
                if fname.is_file():
                    if fname.name!=x:
                        f = open(fname, 'r')
                        n=f.read()
                        if n==v:
                            dup[x].append(fname.name)
            i=i+1
        return(dup)