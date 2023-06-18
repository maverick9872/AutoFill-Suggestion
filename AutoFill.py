class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TrieNode()

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_end_of_word = True

    def search(self, key):
        if not self.root:
            return False

        current = self.root
        for char in key:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.is_end_of_word

    def splay(self, key):
        if not self.root:
            return

        parent = None
        current = self.root

        while True:
            if key == current:
                break
            elif key < list(current.children.keys())[0]:
                if list(current.children.keys())[0] and key < list(current.children.keys())[0]:
                    child = current.children[list(current.children.keys())[0]]
                    if list(child.children.keys())[0] and key < list(child.children.keys())[0]:
                        current.children[list(current.children.keys())[0]] = child.children[list(child.children.keys())[0]]
                        child.children[list(child.children.keys())[0]] = current
                        current = child.children[list(child.children.keys())[0]]
                    else:
                        current.children[list(current.children.keys())[0]] = child.children[list(child.children.keys())[1]]
                        child.children[list(child.children.keys())[1]] = current
                        current = child.children[list(child.children.keys())[1]]
                else:
                    break
            else:
                if list(current.children.keys())[1] and key > list(current.children.keys())[1]:
                    child = current.children[list(current.children.keys())[1]]
                    if list(child.children.keys())[1] and key > list(child.children.keys())[1]:
                        current.children[list(current.children.keys())[1]] = child.children[list(child.children.keys())[1]]
                        child.children[list(child.children.keys())[1]] = current
                        current = child.children[list(child.children.keys())[1]]
                    else:
                        current.children[list(current.children.keys())[1]] = child.children[list(child.children.keys())[0]]
                        child.children[list(child.children.keys())[0]] = current
                        current = child.children[list(child.children.keys())[0]]
                else:
                    break

        if parent:
            if parent.children[list(parent.children.keys())[0]] == current:
                parent.children[list(parent.children.keys())[0]] = current.children[list(current.children.keys())[0]]
                current.children[list(current.children.keys())[0]] = parent
            else:
                parent.children[list(parent.children.keys())[1]] = current.children[list(current.children.keys())[1]]
                current.children[list(current.children.keys())[1]] = parent

        self.root = current

    def autofill(self, prefix):
        if not self.root:
            return []

        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        self.splay(prefix)

        suggestions = []

        def dfs(node, prefix):
            if node.is_end_of_word:
                suggestions.append(prefix)

            for char, child in node.children.items():
                dfs(child, prefix + char)

        dfs(current, prefix)

        return suggestions


# Example usage:
autofill_generator = SplayTree()
words = ["apple", "application", "aptitude", "banana", "bat", "cat"]
for word in words:
    autofill_generator.insert(word)

prefix = "ap"
suggestions = autofill_generator.autofill(prefix)
print("Autofill suggestions for prefix '{}':".format(prefix))
print(suggestions)
