import heapq
from collections import defaultdict

class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.middle = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_trinary_huffman_tree(freq_map):
    priority_queue = []
    for key, value in freq_map.items():
        heapq.heappush(priority_queue, Node(key, value))


    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        middle = heapq.heappop(priority_queue)
        combined_freq = left.freq + middle.freq
        combined_node = Node(None, combined_freq)
        combined_node.left = left
        combined_node.middle = middle

        if priority_queue: 
            right = heapq.heappop(priority_queue)
            combined_freq += right.freq
            combined_node.right = right

        combined_node.freq = combined_freq
        heapq.heappush(priority_queue, combined_node)

    return priority_queue[0]

def encode_trinary_huffman(root, code=''): # generate the codes for each character
    if root is None:
        return {}

    if root.value is not None:
        return {root.value: code}

    codes = {}
    codes.update(encode_trinary_huffman(root.left, code + '0'))
    codes.update(encode_trinary_huffman(root.middle, code + '1'))
    if root.right:
        codes.update(encode_trinary_huffman(root.right, code + '2'))

    return codes

def huffman_encoding_trinary(text):
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1

    if len(freq_map) == 1:
        return {'0': '0'*len(text)}, '0'*len(text)

    root = build_trinary_huffman_tree(freq_map)
    codes = encode_trinary_huffman(root)

    encoded_text = ''.join(codes[char] for char in text)

    print(f'codes are {codes}')
    print(type(codes))

    return codes, encoded_text

def huffman_decoding_trinary(codes, encoded_text):
    # complete this function
    pass

