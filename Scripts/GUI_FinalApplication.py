from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import GraphGUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")

        # setup central widget and main graphics area
        self.MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: powderblue")
        self.graphView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphView.setObjectName("graphView")


        # using the MainWindow passed into the funtion, add a graph scene
        self.scene = self.MainWindow.graph_scene
        self.graphView.setScene(self.scene)
        self.graphView.setStyleSheet("background-color: white")


        # setup layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.graphView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 40, 0, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout2.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout2.setObjectName("verticalLayout2")


        # general label setup
        self.path_status_header = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_status_header.sizePolicy().hasHeightForWidth())
        self.path_status_header.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.path_status_header.setFont(font)
        self.path_status_header.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.path_status_header.setObjectName("path_status_header")
        self.verticalLayout.addWidget(self.path_status_header)
        self.path_algorithm_header_lab = QtWidgets.QLabel(self.centralwidget)


        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_algorithm_header_lab.setFont(font)
        self.path_algorithm_header_lab.setObjectName("path_algorithm_header_lab")
        self.verticalLayout.addWidget(self.path_algorithm_header_lab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        # setup combo box for selecting algorithms to run on graph
        self.select_path_alg_comboBox = SceneConnectedComboBox(self.centralwidget, self.scene)  # box requires reference to scene
        self.select_path_alg_comboBox.setEditable(False)
        self.select_path_alg_comboBox.setStyleSheet("background-color: white")
        self.select_path_alg_comboBox.addItems(['A*', 'BFS','DFS', 'Uniform Cost', 'Greedy'])  # algorithms that can be run
        self.select_path_alg_comboBox.setMaxVisibleItems(8)
        self.select_path_alg_comboBox.setObjectName("select_path_alg_comboBox")
        self.select_path_alg_comboBox.setCurrentIndex(0)
        self.verticalLayout.addWidget(self.select_path_alg_comboBox)  # add combo box to vertical layout

        # setup for algorithm information grid layout
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 5, -1, 5)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(55)
        self.gridLayout.setObjectName("gridLayout")

        # setup internal grid layout for graph status information
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-25, -25, 25, 80)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(55)
        self.gridLayout_2.setObjectName("gridLayout_2")


        self.dist_val_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dist_val_lab.setFont(font)
        self.dist_val_lab.setObjectName("dist_val_lab")
        self.gridLayout.addWidget(self.dist_val_lab, 5, 1, 1, 1)
        self.path_shown_yes_no = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.path_shown_yes_no.setFont(font)
        self.path_shown_yes_no.setObjectName("path_shown_yes_no")
        self.gridLayout.addWidget(self.path_shown_yes_no, 1, 1, 1, 1)
        self.path_shown_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_shown_lab.setFont(font)
        self.path_shown_lab.setObjectName("path_shown_lab")
        self.gridLayout.addWidget(self.path_shown_lab, 1, 0, 1, 1)
        self.node1_val_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.node1_val_lab.setFont(font)
        self.node1_val_lab.setObjectName("node1_val_lab")
        self.gridLayout.addWidget(self.node1_val_lab, 2, 1, 1, 1)
        self.node2__val_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.node2__val_lab.setFont(font)
        self.node2__val_lab.setObjectName("node2__val_lab")
        self.gridLayout.addWidget(self.node2__val_lab, 4, 1, 1, 1)
        self.node1_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.node1_lab.setFont(font)
        self.node1_lab.setObjectName("node1_lab")
        self.gridLayout.addWidget(self.node1_lab, 2, 0, 1, 1)
        self.path_distance_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_distance_lab.setFont(font)
        self.path_distance_lab.setObjectName("path_distance_lab")
        self.gridLayout.addWidget(self.path_distance_lab, 5, 0, 1, 1)
        self.node2_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.node2_lab.setFont(font)
        self.node2_lab.setObjectName("node2_lab")
        self.gridLayout.addWidget(self.node2_lab, 4, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.graph_info_lab = QtWidgets.QLabel(self.centralwidget)


        # large label for graph status information
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.graph_info_lab.setFont(font)
        self.graph_info_lab.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.graph_info_lab.setWordWrap(False)
        self.graph_info_lab.setObjectName("graph_info_lab")
        self.verticalLayout.addWidget(self.graph_info_lab)


        self.node_count_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.node_count_lab.setFont(font)
        self.node_count_lab.setObjectName("node_count_lab")
        self.gridLayout_2.addWidget(self.node_count_lab, 0, 0, 1, 1)

        self.edge_count_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edge_count_lab.setFont(font)
        self.edge_count_lab.setObjectName("edge_count_lab")
        self.gridLayout_2.addWidget(self.edge_count_lab, 1, 0, 1, 1)

        self.num_nodes_val = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.num_nodes_val.setFont(font)
        self.num_nodes_val.setObjectName("num_nodes_val")
        self.gridLayout_2.addWidget(self.num_nodes_val, 0, 1, 1, 1)

        self.num_edges_val = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.num_edges_val.setFont(font)
        self.num_edges_val.setObjectName("num_edges_val")
        self.gridLayout_2.addWidget(self.num_edges_val, 1, 1, 1, 1)

        self.graph_status_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.graph_status_lab.setFont(font)
        self.graph_status_lab.setObjectName("graph_status_lab")
        self.gridLayout_2.addWidget(self.graph_status_lab, 2, 0, 1, 1)

        self.graph_status = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_status.sizePolicy().hasHeightForWidth())
        self.graph_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.graph_status.setFont(font)
        self.graph_status.setObjectName("graph_status")
        self.gridLayout_2.addWidget(self.graph_status, 2, 1, 1, 1)

        self.Graph_control = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Graph_control.setFont(font)
        self.Graph_control.setObjectName("Graph_control")
        self.verticalLayout2.addWidget(self.Graph_control)

        self.add_edge_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.add_edge_lab.setFont(font)
        self.add_edge_lab.setObjectName("add_edge_lab")
        self.verticalLayout2.addWidget(self.add_edge_lab)

        self.Node1_label = QtWidgets.QLabel(self.centralwidget)
        self.Node1_label.setObjectName("Node1")
        self.horizontalLayout_2.addWidget(self.Node1_label)
        self.Node1_labelbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_labelbox.setObjectName("Node1Box")
        self.Node1_labelbox.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_2.addWidget(self.Node1_labelbox)

        self.Node2_label = QtWidgets.QLabel(self.centralwidget)
        self.Node2_label.setObjectName("Node2")
        self.horizontalLayout_2.addWidget(self.Node2_label)
        self.Node2_labelbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_labelbox.setObjectName("Node2Box")
        self.Node2_labelbox.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_2.addWidget(self.Node2_labelbox)

        self.edge_weight = QtWidgets.QLabel(self.centralwidget)
        self.edge_weight.setObjectName("edge_weight")
        self.horizontalLayout_2.addWidget(self.edge_weight)
        self.edge_weight_labelbox = QtWidgets.QLineEdit(self.centralwidget)
        self.edge_weight_labelbox.setObjectName("edge_weight_labelbox")
        self.edge_weight_labelbox.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_2.addWidget(self.edge_weight_labelbox)

        self.verticalLayout2.addLayout(self.horizontalLayout_2)

        self.AddEdge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AddEdge_btn.setObjectName("AddEdge")
        self.verticalLayout2.addWidget(self.AddEdge_btn)

        self.remove_edge_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.remove_edge_lab.setFont(font)
        self.remove_edge_lab.setObjectName("remove_edge_lab")
        self.verticalLayout2.addWidget(self.remove_edge_lab)

        self.Node1RE_label = QtWidgets.QLabel(self.centralwidget)
        self.Node1RE_label.setObjectName("Node1RE")
        self.horizontalLayout_3.addWidget(self.Node1RE_label)

        self.Node1RE_labelbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1RE_labelbox.setObjectName("Node1REBox")
        self.Node1RE_labelbox.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_3.addWidget(self.Node1RE_labelbox)

        self.Node2RE_label = QtWidgets.QLabel(self.centralwidget)
        self.Node2RE_label.setObjectName("Node2RE")
        self.horizontalLayout_3.addWidget(self.Node2RE_label)

        self.Node2RE_labelbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2RE_labelbox.setObjectName("Node2REBox")
        self.Node2RE_labelbox.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_3.addWidget(self.Node2RE_labelbox)

        self.verticalLayout2.addLayout(self.horizontalLayout_3)

        self.delete_edge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_edge_btn.setObjectName("RemoveEdge")
        self.verticalLayout2.addWidget(self.delete_edge_btn)

        self.node_remove_lab = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.node_remove_lab.setFont(font)
        self.node_remove_lab.setObjectName("node_remove_lab")
        self.verticalLayout2.addWidget(self.node_remove_lab)

        self.node_delete = QtWidgets.QLabel(self.centralwidget)
        self.node_delete.setObjectName("node_delete")
        self.horizontalLayout_4.addWidget(self.node_delete)

        self.delete_node = QtWidgets.QLineEdit(self.centralwidget)
        self.delete_node.setObjectName("delete_node")
        self.delete_node.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_4.addWidget(self.delete_node)

        self.verticalLayout2.addLayout(self.horizontalLayout_4)

        self.delete_node_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_node_btn.setObjectName("delete_node_btn")
        self.verticalLayout2.addWidget(self.delete_node_btn)

        self.path_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.verticalLayout2.addWidget(self.path_label)

        self.start_node = QtWidgets.QLabel(self.centralwidget)
        self.start_node.setObjectName("start_node")
        self.horizontalLayout_5.addWidget(self.start_node)

        self.start_node_labelbox = QtWidgets.QLineEdit(self.centralwidget)
        self.start_node_labelbox.setObjectName("start_node_labelbox")
        self.start_node_labelbox.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_5.addWidget(self.start_node_labelbox)

        self.end_node = QtWidgets.QLabel(self.centralwidget)
        self.end_node.setObjectName("end_node")
        self.horizontalLayout_5.addWidget(self.end_node)

        self.end_node_labelbox = QtWidgets.QLineEdit(self.centralwidget)
        self.end_node_labelbox.setObjectName("end_node_labelbox")
        self.end_node_labelbox.setStyleSheet("background-color: lightcyan")
        self.horizontalLayout_5.addWidget(self.end_node_labelbox)

        self.verticalLayout2.addLayout(self.horizontalLayout_5)

        self.show_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_path_btn.setObjectName("show_path")
        self.verticalLayout2.addWidget(self.show_path_btn)

        self.horizontalLayout.addLayout(self.verticalLayout2)
        self.verticalLayout.addLayout(self.gridLayout_2)

        # add vertical layout to main horizontal layout
        self.horizontalLayout.addLayout(self.verticalLayout)

        # set as central widget
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)  # call retranslateUi function
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.button_setup()

    def button_setup(self):

        # connect edit_path_algorithm to combobox
        self.select_path_alg_comboBox.activated.connect(self.edit_path_algorithm)

        # connect update_data function to signal
        self.scene.data_updater.signal.connect(lambda: self.update_data())

        self.AddEdge_btn.clicked.connect(lambda: self.scene.add_edge(self.Node1_labelbox.text(),
                                                                      self.Node2_labelbox.text(),
                                                                      self.edge_weight_labelbox.text()))  # add edge

        self.delete_edge_btn.clicked.connect(lambda: self.scene.remove_edge(self.Node1RE_labelbox.text(),
                                                                            self.Node2RE_labelbox.text()))  # remove edge
        self.show_path_btn.clicked.connect(lambda: self.show_selected_path())

        self.delete_node_btn.clicked.connect(
            lambda: self.scene.remove_node(self.delete_node.text()))  # remove node

    def show_selected_path(self):
        algo = self.scene.current_path_algo  # get the current algorithm being used by GraphScene

        if algo == 'Uniform Cost':
            self.scene.show_uniform_cost_path(self.start_node_labelbox.text(), self.end_node_labelbox.text())
        if algo == 'DFS':
            self.scene.show_DFS_path(self.start_node_labelbox.text(), self.end_node_labelbox.text())
        if algo == 'A*':
            self.scene.show_AStar_path(self.start_node_labelbox.text(), self.end_node_labelbox.text())
        if algo == 'Greedy':
            self.scene.show_Greedy_path(self.start_node_labelbox.text(), self.end_node_labelbox.text())


    def edit_path_algorithm(self):

        # when algorithm combo box is edited reset the graph scenes current algorithm
        self.scene.current_path_algo = self.select_path_alg_comboBox.currentText()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # complete setup of labels and buttons by adding text
        MainWindow.setWindowTitle(_translate("MainWindow", "Informed and Uninformed Searches"))
        self.path_status_header.setText(_translate("MainWindow", "PATH STATUS"))
        self.path_algorithm_header_lab.setText(_translate("MainWindow", "Path Algorithm:"))
        self.dist_val_lab.setText(_translate("MainWindow", "--"))
        self.path_shown_yes_no.setText(_translate("MainWindow", "NO"))
        self.path_shown_lab.setText(_translate("MainWindow", "Path Shown:"))
        self.node1_val_lab.setText(_translate("MainWindow", "--"))
        self.node2__val_lab.setText(_translate("MainWindow", "--"))
        self.node1_lab.setText(_translate("MainWindow", "From Node:"))
        self.Node1_label.setText(_translate("MainWindow", "Node 1"))
        self.Node2_label.setText(_translate("MainWindow", "Node 2"))
        self.edge_weight.setText(_translate("MainWindow", "Weight"))
        self.Node1RE_label.setText(_translate("MainWindow", "Node 1"))
        self.Node2RE_label.setText(_translate("MainWindow", "Node 2"))
        self.node_delete.setText(_translate("MainWindow", "Node"))
        self.start_node.setText(_translate("MainWindow", "Start Node"))
        self.end_node.setText(_translate("MainWindow", "End Node"))
        self.node_remove_lab.setText(_translate("MainWindow", "Delete Node"))
        self.path_distance_lab.setText(_translate("MainWindow", "Distance:"))
        self.node2_lab.setText(_translate("MainWindow", "To Node:"))
        self.add_edge_lab.setText(_translate("MainWindow","Add Edge"))
        self.AddEdge_btn.setText(_translate("MainWindow","Add Edge"))
        self.remove_edge_lab.setText(_translate("MainWindow", "Remove Edge"))
        self.delete_edge_btn.setText(_translate("MainWindow", "Delete Edge"))
        self.delete_node_btn.setText(_translate("MainWindow", "Delete Node"))
        self.show_path_btn.setText(_translate("MainWindow", "Show Path"))
        self.path_label.setText(_translate("MainWindow", "Path"))
        self.Graph_control.setText(_translate("MainWindow", "GRAPH CONTROL"))


    @QtCore.pyqtSlot()
    def update_data(self):
        # function is called when signel is sent indicating the graph has been updated
        _translate = QtCore.QCoreApplication.translate

        if self.scene.path_displayed[
            0]:  # if a path is being displayed indicate that it is and fill in relavent data from graph
            self.path_shown_yes_no.setText(_translate("MainWindow", "YES"))
            self.node1_val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[1])))
            self.node2__val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[2])))
            self.dist_val_lab.setText(_translate("MainWindow", str(self.scene.path_displayed[3])))
        else:  # if no path indicate that nothing is shown
            self.path_shown_yes_no.setText(_translate("MainWindow", "NO"))
            self.node1_val_lab.setText(_translate("MainWindow", "--"))
            self.node2__val_lab.setText(_translate("MainWindow", "--"))
            self.dist_val_lab.setText(_translate("MainWindow", "--"))


class SceneConnectedComboBox(QtWidgets.QComboBox):

    def __init__(self, widget, graph_scene):
        super().__init__(widget)  # initialize a combo box as part of input widget
        self.scene = graph_scene  # include a graph scene reference in combobox
    def keyPressEvent(self, event):
        self.scene.keyPressEvent(event)


class MainGraphWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.graph_scene = GraphGUi(True)  # initialize it with a graph scene
        self.app = QtWidgets.QApplication([])
        self.screen_resolution = app.desktop().screenGeometry()

    def switch_graph_type(self):
        edges = self.graph_scene.edges
        nodes = self.graph_scene.nodes
        digraph = not self.graph_scene.digraph
        self.graph_scene = GraphGUi(digraph)

        return ((nodes, edges))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainGraphWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
