# TreeWidget

## Introduction
* Used for Displaying the nested lists or data trees

## QTreeWidgetItem
* Represents the element of the QTreeWidget

### Constructor

`QTreeWidgetItem(parent, list[str], type)`
Each QTreeWidgetItem represents a column

parent can be QTreeWidgetItem or QTreeWidget


### Methods

#### setters
`add(QTreeWidgetItem)`, `addChildren([QTreeWidgetItem])`, `insertChild(col, QTreeWidgetItem)`, `insertChildren(col, [QTreeWidgetItem])`,
`setBackground(col, QBrush)`, `setForeground(col, QBrush)`, 
`setText(col, str)`, `setData(col, QVarient)`, `setExpanded(bool)`

#### getters

`childCount()`, `child(idx)`, `text(col)`, `data(col)`, `icon(col)`



## QTreeWidget

### Constructor

`QTreeWidget(parent: QtWidgets.QWidget)`


### Methods

#### getters
`addTopLevelItem(QTreeWidgetItem)`, `addTopLevelItems([QTreeWidgetItem])`,
`insertTopLevelItem(index, QTreeWidgetItem)`, `findItems(str, Qt.MatchFlags, col)`, `sortItems(col, QSortOrder)`,


#### setters
`collapseItem(QTreeWidgetItems)`, `expandItem(QtWidgetItem)`, `scrollToItem(QTreeWidgetItem)`


### Signals
`itemChanged(QTreeWidgetItem, col)`, `itemClicked(QTreeWidgetItem)`,
`itemDoubleClicked(QTreeWidgetItem)`, `itemCollapsed(QTreeWidgetItem)`,
`itemExpanded(QTreeWidgetItem)`, `itemSelectionChanged(QTreeWidgetItem)`