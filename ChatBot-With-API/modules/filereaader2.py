import mmap


# ...
def getlastline(fname):
    fname = '/home/abhishek/projects/projects/chatterbot-corpus-master/chatterbot_corpus/data/english/money.yml'
    with open(fname) as source:
        mapping = mmap.mmap(source.fileno(), 0, prot=mmap.PROT_READ)
    return mapping[mapping.rfind(b'\n', 0, -10) + 10:]