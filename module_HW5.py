import pandas as  pd
import networkx as nx
import matplotlib.pyplot as plt
from adjustText import adjust_text
from tqdm import tqdm

class helper_for_HW5:
    #######################################################
    
    def show_hubs(hubs):
        print("\n-->  The HUBS of the NETWORK :\n\t total hubs = {}".format(len(hubs)))
        hubs2 = [(x[0].split("/")[0],x[1]) for x in hubs]
        df = pd.DataFrame(hubs2, columns=['HUBS', 'value'])
        display(df)

    def see_graph_1(graph, hubs, lbl=None):
        
        hubs_nodes = [node for node in graph.nodes if node in [x[0] for x in hubs]]
        not_hubs_nodes = [node for node in graph.nodes if node not in [x[0] for x in hubs]]
        
        plt.figure(figsize=(8,7))
        plt.clf()
        pos = nx.spring_layout(graph)
        nx.draw_networkx_nodes(graph, pos=pos, nodelist=hubs_nodes, node_color='yellow', label='hubs nodes',node_size = 85)
        nx.draw_networkx_nodes(graph, pos=pos, nodelist=not_hubs_nodes, node_color='blue', node_size = 55)
        nx.draw_networkx_edges(graph, pos=pos,  width=0.22,edge_color="black")
        if lbl is not None:
            c = [(x,x.split("/")[0]) for x in graph.nodes]
            nx.draw_networkx_labels(graph, pos,font_size=6.7, font_color='black', labels= dict([(k, v) for k,v in c]), font_weight="bold" )
        plt.legend(scatterpoints = 1, loc = "lower right")
        #plt.margins(x=0.2)
        plt.axis('off')
        plt.show();
    

    def Visualization1_graph1(lista):
        plt.figure(figsize=(10,6))
        plt.barh( [x[0].split("/")[0] for x in lista], [x[1] for x in lista], color='b',align='center')
        plt.yticks(rotation='horizontal', fontsize=7)
        #ax.set_xticklabels(x, fontsize=20)
        plt.grid()
        plt.title("\nNumber of collaborations of each Hero\n")
        plt.xlabel('Collaborations') 
        plt.ylabel('Heros')
        plt.show()
        
    def Visualization1_graph2(heroes_in_comic):  ## good with 34 eroi e 23 fumetti
        print("\nComics considered for visualization : top {} ".format(len(heroes_in_comic)))
        plt.figure(figsize=(11,7))
        plt.barh( [x[0] for x in heroes_in_comic], [x[1] for x in heroes_in_comic], color='b',align='center')
        plt.xticks(rotation= 0)
        plt.grid()
        plt.title("\nNumber of Heroes who appeared in each Comic\n")
        plt.xlabel('Number of Heroes') 
        plt.ylabel('Comics')
        plt.show()
        

    def see_graph_2(sgraph, hubs, jbl=None):

        hubs_nodes = [node for node in sgraph.nodes if node in [x[0] for x in hubs]]
        comic_nodes = [node for node in sgraph.nodes if node not in [x[0] for x in hubs]]
        hero_nodes = [node[0] for node in sgraph.nodes(data=True) if node[1]["type"] == "hero"]
        comic_nodes = [i for i in comic_nodes if i not in hero_nodes]

        plt.figure(figsize=(12,11))
        plt.clf()
        pos = nx.spring_layout(sgraph)
        nx.draw_networkx_nodes(sgraph, pos=pos, nodelist=hero_nodes, node_color='red', label='hero nodes',node_size = 15)
        nx.draw_networkx_nodes(sgraph, pos=pos, nodelist=hubs_nodes, node_color='yellow', label='hubs nodes',node_size = 7)
        nx.draw_networkx_nodes(sgraph, pos=pos, nodelist=comic_nodes, node_color='green', node_size = 3, label="comics")
        if jbl is not None:
            lll = dict([(k, v.split("/")[0]) for k,v in zip(hero_nodes,hero_nodes)])
            nx.draw_networkx_labels(sgraph, pos=pos, font_size=5.6, font_color='black', labels= lll, font_weight=890 )

        nx.draw_networkx_edges(sgraph, pos=pos,width=0.1, edge_color="gray")
        plt.legend(scatterpoints = 1, loc = "upper left")
        #plt.margins(x=0.4)
        plt.axis('off')
        plt.show();
    
    #see_graph_2(sub_graph, hubs)

    
    def plot_degree(dist):
        
        print('\n DEGREE DISTRIBUTION OF THE NETWORK :\n')
        m = max(dist,key=lambda item:item[1])[1]
        m1 = min(dist,key=lambda item:item[1])[1]
        fig = plt.figure(figsize=(14, 7))
        axgrid = fig.add_gridspec(5, 4)
        ax1 = fig.add_subplot(axgrid[3:, :2]);
        ax1.grid()

        ax1.plot([x[1] for x in dist], marker=".", markersize=4, color='tomato'),
        ax1.set_xticks(range(len([x[0] for x in dist])), [x[0].split("/")[0] for x in dist], size='small', rotation=90)
        ax1.tick_params(size=5.5, rotation=90)
        ax1.set_title("Degree Distribution")
        ax1.set_ylabel("Degree")
        ax1.set_xlabel("Nodes")
        ax1.set_ylim(bottom = m1-2, top=m+2)
        plt.show()
        
    def plot_degree_2(dist):
        
        m = max(dist,key=lambda item:item[1])[1]
        print('\n DEGREE DISTRIBUTION:')
        fig = plt.figure(figsize=(18, 10))
        axgrid = fig.add_gridspec(5, 3)
        ax1 = fig.add_subplot(axgrid[3:, :2]);
        ax1.grid()
        ax1.plot([x[1] for x in dist], marker=".", markersize=4, color='tomato'),
        
        text= [ax1.text(i, txt[1], txt[0].split("/")[0], fontsize=6.1,fontweight=305) for i, txt in enumerate(dist) if txt[1] > 100]
        adjust_text(text)
                
        ax1.set_ylim(top=m+135)
        ax1.set_title("Degree Distribution")
        ax1.set_ylabel("Degree")
        ax1.set_xlabel("Nodes")
        plt.show()
        
    def visualization_f5(sub_g, result, ddict):

        com_1 = [node for node in sub_g if node in result[0]]
        com_2 = [node for node in sub_g if node in result[1]]
        plt.figure(figsize=(8,5))
        pos = nx.spring_layout(sub_g)
        nx.draw_networkx_nodes(sub_g, pos=pos, nodelist=com_2, node_color='green', label='community 1',node_size = 85)
        nx.draw_networkx_nodes(sub_g, pos=pos, nodelist=com_1, node_color='red', node_size = 55)
        nx.draw_networkx_edges(sub_g, pos=pos,  width=0.22, edge_color="gray")
        nx.draw_networkx_edges(sub_g, pos, edgelist=sub_g.edges(result[1][0]), width=0.85, edge_color='lightgreen')
        nx.draw_networkx_labels(sub_g, pos,font_size=7.3, font_color='black',labels = ddict)

        plt.axis('off')

        plt.margins(x=0.05)
        plt.show();
        print("\n", result[1][0].split("/")[0], " is the only HERO that's part of a separate community")
        print(" \nMain Community list : \n")
        df = pd.DataFrame([x for x in result[0]], columns=['Community'])
        display(df)
        
    def top_hero_from_graph2(data, Graph, k: int):

        top = data.groupby(['hero'])['hero'].size().sort_values(ascending=False).head(k)
        edges = data.loc[data['hero'].isin(top.keys())]
        edg = list(edges.apply(lambda row: (row['hero'], row['comic']), axis=1))
        sub_graph = nx.edge_subgraph(Graph, edg)
        #print(nx.info(sub_graph))

        return sub_graph, top
    
    
    def short_path(node_list,sub_graph):
        e = [(node_list[i], node_list[i+1]) for i in range(len(node_list)-1)]
        edge_list = [tuple(sorted(x)) for x in e]   ## create the list containing the edges I pass through
        edge_labels = dict([(key, value) for value, key in enumerate(edge_list, 1)])
        
        
        hero_nodes = [node[0] for node in sub_graph.nodes(data=True) if node[1]["type"] == "hero"]
        comic_nodes = [node[0] for node in sub_graph.nodes(data=True) if node[1]["type"] == "comic"]
        #hero_nodes = [hero for hero in hero_nodes if hero not in node_list ]
        comic_nodes = [comic for comic in comic_nodes if comic not in node_list ]

        # I plot the graph and the path
        plt.figure(figsize=(11,10))
        pos = nx.spring_layout(sub_graph)

        nx.draw_networkx_nodes(sub_graph, pos=pos, nodelist=comic_nodes, node_color='blue', label='comic nodes',node_size = 2,alpha=0.40)
        nx.draw_networkx_nodes(sub_graph, pos=pos, nodelist=hero_nodes, node_color='yellow', label='hero nodes', node_size = 5)
        nx.draw_networkx_nodes(sub_graph, pos=pos, nodelist=node_list, node_color='red', label='path',node_size = 12)


        nx.draw_networkx_edges(sub_graph, pos, edgelist=edge_list, width=1.3, edge_color='red')
        nx.draw_networkx_edges(sub_graph, pos=pos,width=0.12, edge_color="gray",alpha=0.18)
        #nx.draw_networkx_edge_labels(sub_graph, pos, edge_labels=edge_labels)
        plt.legend(scatterpoints = 1, loc = "upper left")
        plt.axis('off')
        plt.show()
        
        
    def plot_path(node_lista, s_graph):
        
        people = [node_lista[x] for x in range(0,len(node_lista),2)]
        comic = [node_lista[x] for x in range(0,len(node_lista)) if x % 2 != 0]
        lab = dict([(x,x.split("/")[0]) for x,v in zip(node_lista,node_lista)])
        
        e = [(node_lista[i], node_lista[i+1]) for i in range(len(node_lista)-1)]
        edge_list = [tuple(sorted(x)) for x in e]   ## create the list containing the edges I pass through
        edge_labels = dict([(key, value) for value, key in enumerate(edge_list, 1)])
        
        plt.figure(figsize=(7,6))
        pos = nx.spring_layout(s_graph)
        
        nx.draw_networkx_nodes(s_graph, pos=pos, nodelist=people, node_color='red', label='Hero nodes')
        nx.draw_networkx_nodes(s_graph, pos=pos, nodelist=comic, node_color='lightgreen', label='Comic nodes')

        nx.draw_networkx_edges(s_graph, pos, edgelist =edge_list, edge_color='black')
        nx.draw_networkx_edge_labels(s_graph, pos, edge_labels=edge_labels,font_size=6.9)
        nx.draw_networkx_labels(s_graph, pos, labels = lab, font_size=8.5,font_weight="bold" )
        
        x,y = pos[node_lista[0]]
        plt.text(x,y+0.1,s='Start', bbox=dict(alpha=0.2),fontsize =8,horizontalalignment='center')
        a,b = pos[node_lista[-1]]
        plt.text(a,b+0.1,s='End', bbox=dict(alpha=0.2),fontsize =8,horizontalalignment='center')
        #plt.legend(scatterpoints = 1, loc = "upper right")
        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.1)
        plt.margins(x=0.4)
        plt.axis('off')

        plt.show()
   
 #####################################################################################################
 ################################################################################################àààààà


    

