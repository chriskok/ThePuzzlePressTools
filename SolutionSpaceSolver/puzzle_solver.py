def hamilton(G, size, pt, path=[]):
    print('hamilton called with pt={}, path={}'.format(pt, path))
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(pt, path))
    # loop or dead end, None is implicitly returned

G = {1:[2], 2:[1,3], 3:[2,4], 4:[3]}

print(hamilton(G, 4, 1))