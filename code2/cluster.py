import igraph as ig
from igraph import Graph
from util2 import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--time',type=str,default='0709',help='')
args = parser.parse_args()

adj = np.load(path+'adj_'+args.time+'.npy')
zone_list = np.unique(np.load(path + 'zone.npy')[:,1])
g = Graph.Weighted_Adjacency(adj,mode='plus')
g.vs["name"] = zone_list

result = g.community_multilevel(weights = 'weight')
print(result)

layout = g.layout("drl")

visual_style = {}
visual_style["vertex_size"] = 40
visual_style["vertex_label"] = g.vs["name"]

visual_style["layout"] = layout
visual_style["bbox"] = (1200, 1200)
visual_style["margin"] = 60

ig.plot(result, 'cluster/cluster_'+args.time+'.png', **visual_style, dpi = 500)
