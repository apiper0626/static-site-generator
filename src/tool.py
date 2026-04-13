from textnode import TextType,TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue;
        split_array = old_node.text.split(delimiter)
        if len(split_array) % 2 == 0:
            raise Exception("invalid Markdown syntax")
        for i in range(0, len(split_array)):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_array[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_array[i], text_type))
    return new_nodes