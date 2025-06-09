import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(freq=node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_codes(root):
    codes = {}
    def _build_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        _build_codes(node.left, current_code + "0")
        _build_codes(node.right, current_code + "1")

    _build_codes(root, "")
    return codes

def huffman_encode(text):
    root = build_huffman_tree(text)
    codes = build_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decode(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text

# Ejemplo de uso
if __name__ == "__main__":
    texto = "huffman encoding algorithm"
    codificado, codigos = huffman_encode(texto)
    decodificado = huffman_decode(codificado, codigos)

    print("Texto original:", texto)
    print("Codificado:", codificado)
    print("Decodificado:", decodificado)
    print("Códigos:", codigos)
