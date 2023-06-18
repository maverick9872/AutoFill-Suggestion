# AutoFill-Suggestion
Using simple data structures without using AI/ML/NN for a simple text autofill suggestion generator

Data Structures Used:

1) Tries Tree : Trie is a sorted tree-based data-structure that stores the set of strings. It has the number of pointers equal to the number of characters of the alphabet in each node. It can search a word in the dictionary with the help of the word's prefix.
2) Splay Tree : A splay tree is a self-balancing tree, but AVL and Red-Black trees are also self-balancing trees then. What makes the splay tree unique two trees. It has one extra property that makes it unique is splaying.

Using data structures like Trie and Splay Tree for building an autofill engine offers several advantages compared to AI/ML and neural networks:

Efficiency: Trie and Splay Tree data structures are efficient for searching and retrieving words based on a given prefix. They have fast lookup times, typically O(m), where m is the length of the prefix. This makes them well-suited for real-time autofill suggestions as the user types.

Predictable and deterministic behavior: With Trie and Splay Tree, the suggestions provided are based solely on the available words in the data structure. There is no dependency on training data or statistical models, which can introduce variability and potential biases. The suggestions are consistent and do not change over time unless the underlying data is modified.

Low memory footprint: Trie data structure, in particular, is known for its space efficiency. It can store a large number of words using minimal memory compared to other approaches. This is especially important in resource-constrained environments, such as mobile devices or embedded systems.

Flexibility: Trie and Splay Tree data structures can be customized to support additional functionalities beyond autofill, such as word suggestions based on user history or frequency of occurrence. They provide a foundation upon which additional features can be built and extended as needed.

Offline availability: Once the Trie or Splay Tree is constructed, it can be used offline without requiring an active internet connection or access to a server. This can be advantageous in scenarios where connectivity is limited or when privacy concerns dictate keeping user data local.

It's worth noting that AI/ML and neural network-based approaches can offer their own set of advantages, such as the ability to learn from large amounts of data and adapt to user behavior. They can handle more complex patterns and semantics, making them suitable for applications that require sophisticated language understanding. However, when it comes to simple prefix-based autofill, Trie and Splay Tree data structures provide a lightweight and efficient solution.

Worst Case Time Complexity : n*log(n) [n = no of nodes in the hybrid tree]
