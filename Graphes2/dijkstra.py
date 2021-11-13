def dijkstra (G, depart, fin):
    nbNoeuds = len(G)
    ndsVisites = 0
    distance = np.full((nbNoeuds, nbNoeuds), np.inf)
    for i in range (nbNoeuds):
        np.empty(())
