from refer import *

# it's a block group (derivative QTextBlockGroup)

test = Test()
test.setHtml(
    """
<ol>
    <li> 
        Fruits
        <ol>
            <li> Orange </li>
            <li> Apple </li>
            <li> Banana </li>
        </ol>
    </li>
    <li>
        Vegetables
        <ol>
            <li> Potato </li>
            <li> Tomato </li>
            <li> Carrot </li>
        </ol>
    </li>
</ol>

<p> not a text list </p> 
"""
)

test.show()

root = test.document().rootFrame()

# number of blocks here == total number of items (even sub items) here 9
# so every block here can be converted to a QTextList

count = 0
for child in root:
    count += 1
print(count)  # 8 + 1 (p)


for child in root:
    if child.currentBlock():
        block: QtGui.QTextBlock = child.currentBlock()
        t_list = block.textList()  # getting the text list will be none else

        if not t_list:
            continue

        for _ in range(t_list.count()):
            print(t_list.item(_).text())

        print(22*'-')

    else:
        print(child.currentFrame())

sample.exec_()


"""
other Example:
 
1. fruits
    1. orange
    2. banana
    
2. vegetables
    1. potato
    2. Tomato 

loop
-----
fruits
vegetables

loop
-----
orange
tomato

loop
-----
orange
tomato

loop
-----
fruits
vegetables

loop
-----
potato
Tomato 

here we can see same list repeats whenever we are any one of li of ol
"""