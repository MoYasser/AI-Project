from queue import PriorityQueue



def uniform_cost(graph, from_node, goal_node=None):
  q = PriorityQueue() # create a priority queue
  node_dict = {}  # create a node dictionary to return a distance, parent pair given a node value 
  current = (None, None) # holds the currently selected node
  edge_w = None
  if goal_node is None: goal_node = node_dict.keys() # if no node was input, find path to all nodes

  # make start node is valid	
  if from_node not in graph.nodes_dict:
    print ('Invalid start node of ' + str(from_node))
    return

  for node in goal_node:
    if node not in graph.nodes_dict:
      print ('Invalid end node of ' + str(node))
      return	
    
  # set up algorithm start conditions
  for node in graph.nodes_dict.keys(): # for each node
    if node == from_node: # if node is the start node
      q.put((0, node))  # put node in queue with 0 distance
      node_dict[node] = (0, node) # put into dictionary with 0 distance and itself as a parent
    else:
      node_dict[node] = (float('inf'), None)
  while not q.empty():
    current = q.get() # get node with shortest distance from start
    for adj_node in graph.nodes_dict[current[1]]: # for each adjacent node
      edge_w = graph.edges_dict[(current[1], adj_node)]
      if edge_w < 0: return [('Invalid', -1, None)]
      dist = current[0] + edge_w
      if dist < node_dict[adj_node][0]:
        q.put((dist, adj_node))
        node_dict[adj_node] = (dist, current[1])
    
  result = []
  for node in goal_node: # go through all end nodes
    path = [node] 
    total_dist = node_dict[node][0] # set total distance to dist from start to goal node
    if total_dist == float('inf'): # if path wasn't found
      result.append((node, total_dist, None)) # return result with None 
    else:  
      while path[0] != from_node: # while node at 0 index is not start node
        path.insert(0, node_dict[path[0]][1]) # insert parent into 0 index of path
      result.append((node, total_dist, path)) # add path to result list

  return result	  



