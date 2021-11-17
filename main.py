# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import xml.etree.ElementTree as ET
import sys

neededSave = False


def alter_tree_recursively(root, tag, attrib, value):
    if root.tag == tag:
        if root.attrib.get(attrib) != value:
            root.attrib[attrib] = value
            global neededSave
            neededSave = True
    for child in root:
        alter_tree_recursively(child, tag, attrib, value)


if __name__ == '__main__':
    argv = sys.argv[1:]

    if len(argv) == 4:
        filename, tag_name, attrib_name, value_to_add_or_replace = argv
        print("Filename: ", filename)
        print("Desired tag: ", tag_name)
        print("Attrib to fix: ", attrib_name)
        print("New value: ", value_to_add_or_replace)

        tree = ET.parse(filename)
        root = tree.getroot()
        alter_tree_recursively(root, tag_name, attrib_name, value_to_add_or_replace)

        if neededSave:
            with open(filename, "w+b") as f:
                tree.write(f, encoding='utf-8')
                f.close()
        else:
            print("Nothing to modify!")

        sys.exit(0)
    else:
        print("Insufficent arguments. Sample ./main.py <filename> <tag name> <attribute name> <value to add or replace>")
        sys.exit(1)



