from PyQt5 import QtCore, QtGui, QtWidgets
import GUIGraph as graph
import GraphSearch
from GraphSearch import *
import graph_path_algorithm as path_alg
import math


class Node(QtWidgets.QGraphicsItem):
    def __init__(self, x, y, val, heuristic):

        super().__init__()

        self.x = x  # set x coordinate of node
        self.y = y  # set y coordinate of node
        self.val = val  # set node value
        self.heuristic = heuristic
        self.highlighted = False
        self.selected = False

    def paint(self, painter, option, widget):

        if self.selected:
            # if the node is seleted paint it red
            painter.setPen(QtCore.Qt.black)
            painter.setBrush(QtCore.Qt.palegreen)
        elif self.highlighted:
            # if the node is highlighted paint it green
            painter.setPen(QtCore.Qt.green)
            painter.setBrush(QtCore.Qt.darkGreen)

        else:
            # otehrwise paint it orange
            painter.setPen(QtCore.Qt.darkBlue)
            painter.setBrush(QtCore.Qt.blue)
        # paint the node to the scene
        painter.drawEllipse(self.x, self.y, 35, 35)
        painter.setPen(QtCore.Qt.white)
        painter.setFont(QtGui.QFont('Decorative', (10 / len(str(self.val)) + 5)))
        painter.drawText(QtCore.QRect(self.x, self.y, 35, 35), QtCore.Qt.AlignCenter, self.val)
        painter.setPen(QtCore.Qt.black)  # pen to black
        painter.setFont(QtGui.QFont('Decorative', 11))  # set font
        painter.drawText(QtCore.QRect(self.x, self.y + 30, 50, 40), QtCore.Qt.AlignCenter, 'h = ' + self.heuristic)

    def boundingRect(self):
        return QtCore.QRectF(self.x, self.y, 37, 37)


class Edge(QtWidgets.QGraphicsItem):
    def __init__(self, node1, node2, weight, directed):

        super().__init__()
        self.directed = directed
        self.node1 = node1  # set node at one end of edge
        self.node2 = node2  # set node at other end of edge
        self.x1 = node1.x + 20  # set x coordinate of one end of edge
        self.y1 = node1.y + 20  # set y coordinate of one end of edge
        self.x2 = node2.x + 20  # set x coordinate of other end of edge
        self.y2 = node2.y + 20  # set y coordinate of other end of edge

        self.weight = weight  # set edge weight of edge
        self.midx = (self.x1 + self.x2) / 2  # find midpoint x cooridinate of edge
        self.midy = (self.y1 + self.y2) / 2  # find midpoint y cooridinate of edge
        self.strWeight = str(weight)  # get weight as string
        self.highlighted = False

    def get_directed_arrow_points(self, x1, y1, x2, y2, d):

        # get point for head of arrow--
        v1 = x1 - x2  # x cooridinate for vector between points
        v2 = y1 - y2  # y coordinate for vicot between points

        # to get unit vector requires: u = v/|v|
        dom = math.sqrt(math.pow(v1, 2) + math.pow(v2, 2))  # = |v|
        new_x = v1 / dom  # unit vector x component
        new_y = v2 / dom  # unit vecotr y componenet

        point1 = (x2 + new_x * d, y2 + new_y * d)
        p1x = x2 + new_x * d * 2  # get x value of a point along the edge that is twice as far along the edge as the given node radius d
        p1y = y2 + new_y * d * 2  # get y value of point

        # because we now want a unit vector perpendicular to the original edge
        v2 = x1 - p1x  # switch x and y vector values
        v1 = -(y1 - p1y)  # and negate a vector component

        # to get unit vector requires: u = v/|v|
        dom = math.sqrt(math.pow(v1, 2) + math.pow(v2, 2))  # = |v|

        new_x = v1 / dom  # get unit vector components
        new_y = v2 / dom
        point2 = (p1x + new_x * d / 2.0, p1y + new_y * d / 2.0)  # length from this point to edge is 1/2 radius of node

        return ([point1, point2])  # return a list of the three points

    def paint(self, painter, option, widget):
        pen = QtGui.QPen()
        pen.setWidth(3)
        if self.highlighted:
            # if edge is highlighted paint it green
            pen.setColor(QtCore.Qt.green)
        else:
            # otherwise paint it red
            pen.setColor(QtCore.Qt.gray)
        # paint line to represent edge
        painter.setPen(pen)
        painter.drawLine(self.x1, self.y1, self.x2, self.y2)  # draw line to represent edge

        if self.highlighted:
            # if edge is highlighted paint arrow green
            pen.setColor(QtCore.Qt.green)
            painter.setBrush(QtGui.QColor(165, 255, 0, 255))
            painter.setPen(QtCore.Qt.black)  # pen to black
            painter.setFont(QtGui.QFont('Decorative', 11))  # set font
            painter.drawText(self.midx, self.midy, self.strWeight)
        else:
            # otherwise paint it red

            painter.setPen(QtCore.Qt.black)  # pen to black
            painter.setFont(QtGui.QFont('Decorative', 11))  # set font
            painter.drawText(self.midx, self.midy, self.strWeight)  # draw weight near mipoint of edge

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 2500, 2500)


class GraphGUi(QtWidgets.QGraphicsScene):
    def __init__(self, digraph):
        super().__init__()
        self.digraph = digraph
        self.setSceneRect(0, 0, 1200, 900)  # set size of graphical scene
        self.nodes = {}  # node dictionary
        self.edges = {}  # edge dictionary
        self.graph = graph.Graph_GUI(self.digraph)  # graph object to underlay the graphical interface
        self.gs = GraphSearch.Graph()

        self.path_displayed = (False, 'NONE', 'NONE', '-')  # initialize information about displayed path
        self.current_path_algo = 'Uniform Cost'  # set current path algorithm being used to DIJKSTRA

        self.data_updater = UpdateData()  # create a data updater to send out a signal anytime data about the graph is changed

        # set up message box for displaying invalid input alerts
        self.InvalidInMsg = QtWidgets.QMessageBox()
        self.InvalidInMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.InvalidInMsg.setWindowTitle('Invalid input alert!')

        self.selected = []

    def check_selected(self, requiredNum):

        if len(self.selected) != requiredNum:  # if nodes arent selected print message and cancel
            return False

        return True

    def deselect_nodes(self):
        for node in self.selected:
            node.selected = False
        self.selected = []

    def mousePressEvent(self, event):

        if event.button() != QtCore.Qt.LeftButton:  # if right button pressed
            self.select_node(event)  # call selectd node function
            return

        self.add_node(event)  # otherwise call add node function

        QtWidgets.QGraphicsScene.mousePressEvent(self, event)  # call original function to maintain functionality

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Return:  # if enter is pressed
            self.add_edge_selected()  # try to connect selected nodes with an edge
        elif event.key() == QtCore.Qt.Key_Backspace:  # if backspace pressed
            self.delete_nodes_selected()
        elif event.key() == QtCore.Qt.Key_Up:  # if up arrow pressed
            self.display_path()
        elif event.key() == QtCore.Qt.Key_Down:  # if down arrow pressed
            self.delete_shortest_path()  # set shortest path between node to no longer be visible
        elif event.key() == QtCore.Qt.Key_Delete:  # if delete pressed
            self.delete_edge_selected()  # remove edge between selected nodes

        self.update()

    def delete_edge_selected(self):

        if self.check_selected(2):  # if nodes selected
            self.remove_edge(self.selected[0].val, self.selected[1].val)  # delete edge between them
            self.deselect_nodes()  # deselect nodes
        else:  # else print error message
            self.InvalidInMsg.setText('Must select 2 nodes to delete edge')
            self.InvalidInMsg.exec_()

    def add_edge_selected(self):
        # check that 2 nodes selected
        if self.check_selected(2):  # if nodes selected

            weight, ok = QtWidgets.QInputDialog.getText(QtWidgets.QWidget(), 'Input edge weight',
                                                        'Enter weight of edge:')  # use dialog to get weight of edge between nodes
            if ok:
                if self.add_edge(self.selected[0].val, self.selected[1].val, weight):  # add edge between selected nodes
                    self.deselect_nodes()  # deselect nodes
        else:  # if invalid selection p rint error
            self.InvalidInMsg.setText('Must select 2 nodes to add edge')
            self.InvalidInMsg.exec_()

    def delete_nodes_selected(self):
        for node in self.selected:  # for each of the selected nodes
            self.remove_node(node.val)  # remove it from the graph

        self.selected = []

    def select_node(self, event):
        node = self.itemAt(event.scenePos(), QtGui.QTransform())  # get item clicked on at this position in scene

        if type(node) is Node:  # if item is a node
            node.selected = not node.selected  # set selected to True
            if node.selected:
                self.selected.append(node)
            else:
                self.selected.remove(node)
        self.update()

    def add_node(self, event):
        x = event.scenePos().x()  # get x position of mouse
        y = event.scenePos().y()  # get y position of mouse

        node_val, ok = QtWidgets.QInputDialog.getText(QtWidgets.QWidget(), 'Enter Node info',
                                                      'Enter node name:')  # use dialog to get node value to be added

        if ok:  # dialog value was input
            if len(str(node_val)) < 5 and len(str(node_val)) > 0:  # if input was between 1 and 4 characters
                nodeH, ok = QtWidgets.QInputDialog.getText(QtWidgets.QWidget(), 'Enter Node info',
                                                           'Enter node heuristic:')
                connections = []
                path_shown = self.path_displayed[0]  # get whether or not a shortest path is currently displayed
                self.delete_shortest_path()
                if node_val in self.nodes:
                    connections = self.remove_node(node_val)  # remove original node and save all its node connections

                node = Node(x - 20, y - 20, str(node_val), nodeH)  # create a new node at the given x and y coordinates
                self.addItem(node)  # add node to scene
                self.nodes[node.val] = node  # add node to node dictionary
                self.graph.add_node(node.val)  # add node value to underlying graph objects
                self.graph.add_node(node.heuristic)
                self.gs.add_vertex(int(node_val), int(nodeH))
                for connection in connections:  # for each of the original node connections
                    self.add_edge(connection[0], connection[1], connection[2])  # add the original edges

            else:
                self.InvalidInMsg.setText(
                    'Node name must consist of between 1 and 4 characters')  # print message if invalid dialog input
                self.InvalidInMsg.exec_()
                return

            # reset path displayed variable to reflect its original value before node was added
            self.path_displayed = (path_shown, self.path_displayed[1], self.path_displayed[2], self.path_displayed[3])
            if self.path_displayed[0]:  # if path was displayed before node was added
                self.reset_path()  # find and display path

            self.data_updater.signal.emit()  # emit a signal to notify that the graph was updated

    def add_edge(self, node1_val, node2_val, weight):

        try:
            numWeight = int(weight)  # try to convert weigth to an integer
        except ValueError:  # value error exception if unable to cast weight as a float
            self.InvalidInMsg.setText('Weight must be a number')
            self.InvalidInMsg.exec_()
            return False

        if node1_val not in self.nodes:  # ensure node value is in dictionary of nodes
            self.InvalidInMsg.setText('"' + str(node1_val) + '" is not in graph')
            self.InvalidInMsg.exec_()
            return False
        if node2_val not in self.nodes:  # ensure node value is in dictionary of nodes
            self.InvalidInMsg.setText('"' + str(node2_val) + '" is not in graph')
            self.InvalidInMsg.exec_()
            return False
        if node2_val == node1_val:  # ensure node values are unique
            self.InvalidInMsg.setText('Two unique node values required to create an edge')
            self.InvalidInMsg.exec_()
            return False

        # get nodes from dictionary
        node2 = self.nodes[node2_val]
        node1 = self.nodes[node1_val]

        path_shown = self.path_displayed[0]  # save whether shortest path is being shown
        self.delete_shortest_path()  # delete shortest path
        if (node1_val, node2_val) in self.edges or ((node2_val,
                                                     node1_val) in self.edges and not self.digraph):  # if edge already exists between given nodes
            self.remove_edge(node1_val, node2_val)  # remove edge

        edge = Edge(node1, node2, numWeight, self.digraph)  # create new edge

        self.addItem(edge)  # add edge to scene
        self.graph.add_edge(node1.val, node2.val, numWeight)  # add edge to underlying graph
        self.gs.add_edge(int(node1_val), int(node2_val), numWeight)
        # reset all nodes in graph so they are layered over the edges
        for val, node in self.nodes.items():
            self.removeItem(node)
            self.addItem(node)

        self.edges[(node1_val, node2_val)] = edge  # add new edge to list of edges

        self.path_displayed = (path_shown, self.path_displayed[1], self.path_displayed[2],
                               self.path_displayed[3])  # reset path displayed value
        if self.path_displayed[0]:  # if path was displayed before adding the edge
            self.reset_path()  # find and display path
        self.data_updater.signal.emit()  # emit a signal to notify that the graph was updated
        return True  # return true if edge successfully added

    def remove_edge(self, node1_val, node2_val):

        if node1_val not in self.nodes:  # if node1_val not in nodes dictinary
            self.InvalidInMsg.setText('"' + str(node1_val) + '" is not in graph')
            self.InvalidInMsg.exec_()  # print message and exit
            return

        if node2_val not in self.nodes:  # if node1_val not in nodes dictinary
            self.InvalidInMsg.setText('"' + str(node2_val) + '" is not in graph')
            self.InvalidInMsg.exec_()  # print message and exit
            return

        if (node1_val, node2_val) not in self.edges:  # if edge from node1_val to node2_val not in edges dictionary
            if self.digraph or (
                    node2_val,
                    node1_val) not in self.edges:  # and edge from node2_val to node1_val not in edges dictionary
                self.InvalidInMsg.setText('No edge exists between nodes ' + str(node1_val) + ' and ' + str(node2_val))
                self.InvalidInMsg.exec_()  # print message and exit
                return
            else:
                edge = self.edges[(node2_val, node1_val)]  # otherwise represent edge from node2_val, node1_val
        else:
            edge = self.edges[(node1_val, node2_val)]  # otherwise represent edge from node1_val, node2_val

        path_shown = self.path_displayed[0]  # save whether shortest path is being shown
        self.delete_shortest_path()  # delete shortest path

        self.removeItem(edge)  # remove edge from scene
        self.graph.remove_edge(node1_val, node2_val)  # remove edge from underlaying graph

        del self.edges[(edge.node1.val, edge.node2.val)]  # delete edge from edges dictionary

        self.path_displayed = (path_shown, self.path_displayed[1], self.path_displayed[2], self.path_displayed[3])
        if self.path_displayed[0]:  # if path was being displayed
            self.reset_path()  # find shortest path

        self.data_updater.signal.emit()  # emit a signal to notify that the graph was updated

    def remove_node(self, node_val):

        if node_val not in self.nodes:  # if node value not in dictionary
            self.InvalidInMsg.setText(str(node_val) + ' is not in graph')
            self.InvalidInMsg.exec_()  # print message and exit
            return

        path_shown = self.path_displayed[0]  # save whether shortest path is being shown
        self.delete_shortest_path()  # delete shortest path

        connections = []
        for node_pair in self.edges.keys():  # for each edge in graph
            if node_pair[0] == node_val or node_pair[1] == node_val:  # if edge connects to this node
                connections.append(
                    (node_pair[0], node_pair[1], self.edges[node_pair].weight))  # save the connection in list

        for connection in connections:  # for all connections
            self.remove_edge(connection[0], connection[1])  # remove edges from graph

        self.removeItem(self.nodes[node_val])  # remove the node from the scene
        self.graph.remove_node(node_val)  # remove the node from the underlaying graph
        del self.nodes[node_val]  # delete the node from the node dictionary

        self.path_displayed = (path_shown, self.path_displayed[1], self.path_displayed[2], self.path_displayed[3])
        if self.path_displayed[0]:  # if the shortest path was being displayed
            self.reset_path()  # find shortest path with edited graph

        self.data_updater.signal.emit()  # emit a signal to notify that the graph was updated
        return connections  # return the connections that were deleted

    def show_uniform_cost_path(self, from_node_val, to_node_val):
        self.delete_shortest_path()  # delete shortest path of currently displayed
        path = None

        if from_node_val not in self.nodes or to_node_val not in self.nodes:  # nodes for path not in nodes dictionary
            self.InvalidInMsg.setText('Invalid node value input')
            self.InvalidInMsg.exec_()
            return

        short_path_info = path_alg.uniform_cost(self.graph, from_node_val, [to_node_val])[0]

        if short_path_info[1] == 0:
            return
        path = short_path_info[2]  # get the path list from running that path search

        if path == None:  # if no path
            self.InvalidInMsg.setText(
                'No path exists between nodes "' + str(from_node_val) + '" and "' + str(to_node_val) + '"')
            self.InvalidInMsg.exec_()  # show message # deselect nodes in graph and exit
            self.update()
            return
        node_val = None

        while len(path) > 1:  # while length of path if greater than 1
            node_val = path.pop(0)  # remove first item from path
            self.nodes[node_val].highlighted = True  # highlight that node
            if len(path) > 0:  # if length of path is still greater than 0
                if (node_val, path[0]) in self.edges:  # and edge exists between current node value and next in path
                    self.edges[(node_val, path[0])].highlighted = True  # highlight the edge
                else:
                    self.edges[(path[0],
                                node_val)].highlighted = True  # else the edge exists as being from next in path to current node
        self.nodes[path[0]].highlighted = True  # highlight the last node in the path

        if self.digraph:
            self.overlay_highlighted()
            self.update()
            self.path_displayed = (
                True, from_node_val, to_node_val, str(short_path_info[1]))  # reset path displayed information
            self.data_updater.signal.emit()  # emit a signal to notify that the graph was updated

    def show_DFS_path(self, start_node, goal_node):
        self.delete_shortest_path()  # delete shortest path of currently displayed
        path = None

        if start_node not in self.nodes or goal_node not in self.nodes:  # nodes for path not in nodes dictionary
            self.InvalidInMsg.setText('Invalid node value input')
            self.InvalidInMsg.exec_()  # show message and exit
            return

        # short_path_info = path_alg.BFS(self.graph, start_node, [goal_node])[0]
        short_path_info = self.gs.DFS(int(start_node), int(goal_node))
        if short_path_info[1] < 0:
            return
        path = short_path_info.copy()
        if path == None:  # if no path
            self.InvalidInMsg.setText(
                'No path exists between nodes "' + str(start_node) + '" and "' + str(goal_node) + '"')
            self.InvalidInMsg.exec_()  # show message # deselect nodes in graph and exit
            self.update()
            return
        node_val = None
        while len(path) > 1:  # while length of path if greater than 1
            node_val = str(path.pop(0))  # remove first item from path
            self.nodes[node_val].highlighted = True  # highlight that node
        self.nodes[str(path[0])].highlighted = True  # highlight the last node in the path

    def show_BFS_path(self, start_node, goal_node):
        self.delete_shortest_path()  # delete shortest path of currently displayed
        path = None

        if start_node not in self.nodes or goal_node not in self.nodes:  # nodes for path not in nodes dictionary
            self.InvalidInMsg.setText('Invalid node value input')
            self.InvalidInMsg.exec_()  # show message and exit
            return

        short_path_info = self.gs.BFS(int(start_node), int(goal_node))
        if short_path_info[1] < 0:
            return
        path = short_path_info.copy()
        if path == None:  # if no path
            self.InvalidInMsg.setText(
                'No path exists between nodes "' + str(start_node) + '" and "' + str(goal_node) + '"')
            self.InvalidInMsg.exec_()  # show message # deselect nodes in graph and exit
            self.update()
            return
        node_val = None
        while len(path) > 1:  # while length of path if greater than 1
            node_val = str(path.pop(0))  # remove first item from path
            self.nodes[node_val].highlighted = True  # highlight that node
        self.nodes[str(path[0])].highlighted = True  # highlight the last node in the path

    def show_AStar_path(self, start_node, goal_node):
        self.delete_shortest_path()  # delete shortest path of currently displayed
        path = None
        node1 = self.gs.set_start(int(start_node))
        node2 = self.gs.set_goal(int(goal_node))
        short_path_info = self.gs.A_star(int(start_node))
        if short_path_info[1] < 0:
            return
        path = short_path_info.copy()
        if path == None:  # if no path
            self.InvalidInMsg.setText('No path exists between nodes "' + str(node1) + '" and "' + str(node2) + '"')
            self.InvalidInMsg.exec_()  # show message # deselect nodes in graph and exit
            self.update()
            return
        node_val = None
        while len(path) > 1:  # while length of path if greater than 1
            node_val = str(path.pop(0))  # remove first item from path
            self.nodes[node_val].highlighted = True  # highlight that node
            if len(path) > 0:  # if length of path is still greater than 0
                if (
                        node_val,
                        str(path[0])) in self.edges:  # and edge exists between current node value and next in path
                    self.edges[(node_val, str(path[0]))].highlighted = True  # highlight the edge
                else:
                    self.edges[(str(path[0]),
                                node_val)].highlighted = True  # else the edge exists as being from next in path to current node
        self.nodes[str(path[0])].highlighted = True  # highlight the last node in the path

        if self.digraph: self.overlay_highlighted()
        self.update()
        self.path_displayed = (True, start_node, goal_node, str(self.gs.cost))
        self.data_updater.signal.emit()

    def show_Greedy_path(self, start_node, goal_node):
        self.delete_shortest_path()  # delete shortest path of currently displayed
        path = None
        node1 = self.gs.set_start(int(start_node))
        node2 = self.gs.set_goal(int(goal_node))
        short_path_info = self.gs.greedy_search(int(start_node))
        if short_path_info[1] < 0:
            return
        path = short_path_info.copy()
        if path == None:  # if no path
            self.InvalidInMsg.setText('No path exists between nodes "' + str(node1) + '" and "' + str(node2) + '"')
            self.InvalidInMsg.exec_()  # show message # deselect nodes in graph and exit
            self.update()
            return
        node_val = None
        while len(path) > 1:  # while length of path if greater than 1
            node_val = str(path.pop(0))  # remove first item from path
            self.nodes[node_val].highlighted = True  # highlight that node
            if len(path) > 0:  # if length of path is still greater than 0
                if (
                        node_val,
                        str(path[0])) in self.edges:  # and edge exists between current node value and next in path
                    self.edges[(node_val, str(path[0]))].highlighted = True  # highlight the edge
                else:
                    self.edges[(str(path[0]),
                                node_val)].highlighted = True  # else the edge exists as being from next in path to current node
        self.nodes[str(path[0])].highlighted = True  # highlight the last node in the path

        if self.digraph: self.overlay_highlighted()
        self.update()
        self.path_displayed = (True, start_node, goal_node, str(self.gs.cost))
        self.data_updater.signal.emit()

    def delete_shortest_path(self):
        for val, node in self.nodes.items():  # for each node in nodes dictionary
            node.highlighted = False  # remove node highlights

        for val, edge in self.edges.items():  # for each edge
            edge.highlighted = False  # remove highlights

        self.update()
        self.path_displayed = (
            False, self.path_displayed[1], self.path_displayed[2], self.path_displayed[3])  # path info not shown
        self.data_updater.signal.emit()  # emit a signal to notify that the graph was updated

    def set_current_path_algo(self, algo):
        # setter to change the currently selected graph algorithm
        self.current_path_algo = algo

    def reset_path(self):
        # function to be used on graphs that are updated
        if self.current_path_algo == 'Uniform Cost':
            self.show_uniform_cost_path(self.path_displayed[1], self.path_displayed[2])
        elif self.current_path_algo == 'DFS':
            self.show_DFS_path(self.path_displayed[1], self.path_displayed[2])
        elif self.current_path_algo == 'BFS':
            self.show_BFS_path(self.path_displayed[1], self.path_displayed[2])
        elif self.current_path_algo == 'A*':
            self.show_AStar_path(self.path_displayed[1], self.path_displayed[2])
        elif self.current_path_algo == 'Greedy':
            self.show_Greedy_path(self.path_displayed[1], self.path_displayed[2])

        self.update()

    def overlay_highlighted(self):
        for (from_node_val, to_node_val), edge in self.edges.items():
            if edge.highlighted:
                self.removeItem(edge)
                self.addItem(edge)  # layer highlighted edges over none highlighted edges

        for node_val, node in self.nodes.items():
            # layer all nodes over edges
            self.removeItem(node)
            self.addItem(node)


class UpdateData(QtCore.QObject):
    # class for signaling main window of updated data
    signal = QtCore.pyqtSignal()
