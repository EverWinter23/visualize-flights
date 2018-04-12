'''
12th april 2018 thursday
i swear this time i mean it...
'''

class DirGraph:
    """
    v        stores number of vertices in the graph
    e         stores number of edges in the graph
    """
    def __init__(vertices):
        self.v = vertices
        self.adj = [[] for i in range(v)]

    # directed graph
    def add_route(self, src, dst):
        self.adj[src].append(dst)

    def __str__(self):
        for i in range(self.vertices):
            print("vertex {}: ".format(i), end='')
            for j in self.adj[i]:
                print("{}-->".format(j), end='')
            print("NULL")
        return ''


    




