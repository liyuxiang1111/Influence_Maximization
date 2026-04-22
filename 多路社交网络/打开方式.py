file_path = '/multiplex_network.pickle'
    # file_path = '../Real_Dataset/epinion_multiplex_network_extended.pickle'
    # 替换成自己的路径
with open(file_path, 'rb') as f:
  graphs, multiplex = pickle.load(f)