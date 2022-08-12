questions = { "What is good Code?": "Good code can be define by two factors, \n\t"
                                    "1) It is readable. \n\t"
                                    "2) It is scalable",
              "What is Big O notation?": "Big O notation is how long a code takes to run regardless of CPU. \n\t"
                                         "It involves time complexity and operational complexity. \n\t"
                                         "Algorithm efficiency in Big O is define by Operations (Y-axis) vs Elements (X-axis)",
              "What is Big O of O(n)?":"O(n) is linear complexity, for every operation the amount of elements goes up respectively.",
              "What is Big O of O(1)?": "O(1) is quite efficient as it represents constant time. \n\t"
                                        "We are only doing 1 thing, no matter what constant out put i.e.: O(2),O(100), O(1)",
              "What are the 4 rules in the Big O rule book?": "1) Worst Case - even if we have a break statement, worst case loop will go through all elements, we compute worst case scenarios.\n"
                                                              "2) Remove Constants - all constants are remove in our Big O computations. \n\t"
                                                              " i.e.: O(1+n/2+100) -simplifies-> O(n+1) -further simplifies-> O(n) \n"
                                                              "3) Different terms for Inputs. \n\t"
                                                              " i.e.: def Hello(x,x2) -two inputs-> O(x + x2) -nested loops use multiplication->O(n*n) or O(n^2) \n\t"
                                                              " O(n^2) is horrible time complexity.\n"
                                                              "4) Drop non dominant \n \t"
                                                              "i.e.: O(n+n^2) -simplifies to-> O(n^2)",
              "What time complexity is O(n!)":"Big O notation of O(n!) is horrible and we will probably never see it in our codes. n factorial.",
              "Define scalable code?": "Scalable is define by two things. \n\t"
                                       "1) Speed - Big O (how many operations does it cost) time complexity \n\t"
                                       "2) Memory - Space complexity.",
              "How do we handle Big O in our coding practice":"As a good developer we need to analyze the problem and find a sweet spot between \n"
                                                              "runtime, space and readability.\n"
                                                              "There is a trade of in Big O between time complexity and space complexity.",
              "What are the most important skills for a developer to have.":"Big companies are looking for a person who has \n"
                                                                            "Analytical Skills \n"
                                                                            "Coding Skills \n"
                                                                            "Technical Skills \n"
                                                                            "Communication Skills.",
              "Define a Data structure?":"A Data Structure is a collection of values.",
              "Why do we have different Data Structures.":"Each Data Structure is good for specific things.\n\t"
                                                          "i.e: A Backpack is different from a Fridge which in turn is different from a tool shed.\n\t"
                                                          "We can think of data structures as a container to organize data.",
              "What are some common Data Structures.":"1) Arrays\n"
                                                      "2) Trees\n"
                                                      "3) Stacks\n"
                                                      "4) Tries\n"
                                                      "5) Queues\n"
                                                      "6) Linked Lists\n"
                                                      "7) Graphs\n"
                                                      "8) Hash Tables",
              "What are the Data Structure Actions on RAM?": "1) Insertion - adding item\n"
                                                             "2) Deletion - deleting item\n"
                                                             "3) Traversal - loop through each ram shelf\n"
                                                             "4) Searching - find location of data value\n"
                                                             "5) Sorting - Data that is stored\n"
                                                             "6) Access - accesing data values, these is the most important when choosing which data structure to use.",
              "What is an Array or List":"An array is a data structure which is static in size.\n\t"
                                         "In python the automatically resize memory. Overall the python language doesn't have much control over memory.",
              "What are the Pros of an Array?":"1) Fast lookups.\n"
                                               "2) Fast push/pop \n"
                                               "3) Arrays are can be Ordered",
              "What are the Cons of an Array?":"1) Slow at insert\n"
                                               "2) Slow deletions\n"
                                               "3) Fixed size* caveat for python as they resize memory automatically.",
              "What is the Big O notation of Arrays?":"1) search - O(n) - Fair \n"
                                                      "2) insert - O(n) - Fair \n"
                                                      "3) lookup - O(1) - Good \n"
                                                      "4) delete - O(n) - Fair",
              "In python what is an interesting tip bit for Dictionaries (Hash Tables)?":"Python programming language has made Dictionaries ordered by default.\n"
                                                                                         "sets are not ordered yet.",
              "What is a Hash function?":"A hash function is simply a function that generates a value of fix length for each input that it gets.\n"
                                         "\t It has a input and a value-output that do not change they are idempotent.\n\t"
                                         "It is also a one way only function.",
              "What are some positives of a hash functions?":"Hash functions are big O time complexity of O(1) - constant\n"
                                                             "It can access data really fast",
              "What are the Hash functions actions Big O complexity?":"1) insert - O(1) - Good/Excellent\n"
                                                                      "2) lookup - O(1) - Good/Excellent\n"
                                                                      "3) delete - O(1) - Good/Excellent\n"
                                                                      "4) search - O(1) - Good/Excellent",
              "What is data collision?":"Data collisions occur when data is stored in the same bucket (location) \n"
                                        "Link list are a solution where one data location or 'node' points to another 'node'\n"
                                        "essentially linking both nodes or data locations.\n\t"
                                        "Keep in mind that with hash tables we cannot avoid these collisions, there are a ton of different ways to solve a collision",
              "What is the load factor for hash tables":"O(n/k)",
              "What are the Hash tables actions Big O complexity?":"1) Search - O(1) - Good/Excellent\n"
                                                                   "2) Insert - O(1) - Good/Excellent\n"
                                                                   "3) Lookup - O(1) - Good/Excellent\n"
                                                                   "4) Delete - O(1) - Good/Excellent",
              "What is a linked list?":"An ordered set of data elements, each containing a link to its successor (and sometimes its predecessor.)",
              "How many type of linked lists are there?":"There are two types of linked list which are:\n\t"
                                                         "1) Singley\n\t"
                                                         "2) Doubley",
              "What are the linked list Big O complexity actions?":"1) Prepend O(1) - Good/Excellent \n"
                                                                   "2) Append O(1) - Good/Excellent \n"
                                                                   "3) lookup O(n) - Fair \n"
                                                                   "4) insert O(n) - Fair \n"
                                                                   "5) delete O(n) - Fair \n",
              "What are some draw backs in the linked list, data structure?":"The drawback is the while loop it uses for lookup, insert, remove. Give yous a Big O time complexity of O(n) - Fair",
              "What is a doubly linked list?":" A doubly linked list has an extra point, pointing back to the previous node.\n\t"
                                              "Doubly linked list have pointers from head to tail and tail to head.",
              "What is a singly linked list?":" A singly linked list has single pointers going from head to tail.",
              "What are the pros of linked lists?":"Pros of a linked list are:\n\t"
                                                   "1) Fast Insertion\n\t"
                                                   "2) Fast Deletion\n\t"
                                                   "3) Ordered\n\t"
                                                   "4) Flexible in size - this data structure is best to grow and shrink as needed\n\t\t"
                                                   "i.e: browser history is a perfect application. ",
              "What are the cons of a linked lists?":"Cons of a linked list are:\n\t"
                                                     "1) Slow lookup\n\t"
                                                     "2) More memory usage.",
              "Are Stacks and Queues linear data structures?":"Yes, Stacks and Queues are linear data structures\n\t"
                                                              "They allow us to traverse thru data sequentially. One by One",
              "What is the key difference between Stacks and Queues?":"They are very similar the key difference is how each data structure removes data.",
              "Overall what can you really access in Stacks and Queues?":"Stacks and Queues can really only access the first and last data objects of data.",
              "Why is the limited ability on data structures good, i.e. Stacks + Queues?":"The limited ability can be a useful function,\n\t"
                                                                                          "It allows the developer be assured that the data structure will work only in the way they want.\n\t"
                                                                                          "'We do not want to hand over the whole tool chest'",
              "What is a great example for the way Stacks act and what is this referred as?":"Stacks act like plates being stacked on top of each other.\n\t"
                                                                                             "These is called LIFO or Last In First Out.",
              "What is stack overflow the result of?":"Stack overflow is the result of bad code.\n\t"
                                                      "The most-common cause of stack overflow is excessively deep or infinite recursion.\n\t"
                                                      "which a function calls itself so many times that the space needed to store variables and information associated\n\t"
                                                      "with each call is more than can fit on the stack.",
              "What is an example of LIFO applications in the real world?":" A application example of LIFO is browser history\n\t"
                                                                           "Forward and back button or \n\t"
                                                                           "the Undo/Redo button.",
              "What are the stacks methods and big O time complexity, respectively?":"1) lookup - O(n) - Fair\n"
                                                                                     "2) pop - O(1) - Good/Excellent\n"
                                                                                     "3) push - O(1) - Good/Excellent\n"
                                                                                     "4) peek - O(1) - Good/Excellent.",
              "What is a great example for the way Queues act and what is this referred as?":"One can think of Queues as individuals waiting in line for a rollercoster,\n\t"
                                                                                             "These is opposite of stacks, it is First In First Out or FIFO.",
              "What are some examples of Queues applications in real life?":"Some examples for Queues in real life are\n"
                                                                            "Any wait-list app for tickets i.e. ticket master,\n"
                                                                            "Restaurant app to check in and get a table,\n"
                                                                            "Printers and the printing log,\n"
                                                                            "Uber uses Queues as well",
              "What are the Queues methods and big O time complexity, respectively?":"1) lookup - O(n) - Fair\n"
                                                                                     "2) enqueue - O(1) - Good/Excellent\n"
                                                                                     "3) dequeue - O(1) - Good/Excellent\n\t"
                                                                                     "dequeue is where stacks and queue differ the most.\n\t"
                                                                                     "dequeue is similar to pop, but it doesn't remove the last data value it removes the first 'FIFO'\n"
                                                                                     "4) peek - O(1) - Good/Excellent\n\t"
                                                                                     "Returns the first data value in the Queue",
              "What is an inefficiency seen in arrays that can be solve with Queues?":"In an Array when you remove the first data value\n"
                                                                                       "it will cause all the data values to shift one over,iterating through all the data values - O(n).\n"
                                                                                       "Queues do not, the following data value becomes the Head node and its finish.",
              "What are the pros of Stacks and Queues?":"The pros of Stacks and Queues are:\n\t"
                                                        "1) Fast Operations\n\t"
                                                        "2) Fast Peek\n\t"
                                                        "3) Ordered",
              "What are the cons of Stacks and Queues?":"The cons of Stacks and Queues are:\n\t"
                                                        "1) Slow look ups",
              "Define the data structure known as Trees?":"A tree is a hierarchical data structure defined as a collection of nodes.\n\t"
                                                          "It involves parent child relationships that go one way.\n\t"
                                                          "We also have leaf nodes or sub-childs",
              "What is known ast AST?":"AST is Abstract Syntax Tree\n\t"
                                       "AST are use to depict how codes are built.\n\t"
                                       "Each node of the tree denotes a construct occurring in the code.",
              "How are Tree data structure similar to link lists?":"Tree data structure uses the same principle as linked lists, they use nodes.\n\t"
                                                                   "Basically linked lists are the building blocks (essentially a form of a tree) for Tree data structures.",
              "What are some of the most-common trees that get used? (90% of the time)":"The most-common form of trees used are:\n\t"
                                                                                        "1) Linked lists - singly and doubly\n\t"
                                                                                        "2) Binary Trees",
              "What are the rules attached to a Binary Tree?":"These are the rules to construct a Binary Tree:\n\t"
                                                              "1) Each node can only have 0,1 or 2 nodes\n\t"
                                                              "2) Each child can only have one parent \n\t"
                                                              "3) Each node expresses a certain state",
              "What is a perfect Binary Tree?":"In a perfect Binary Tree all the leaf nodes are full a node has either 0 or 2 child-nodes.",
              "What methods/actions are Binary Trees efficient at?":"Binary Trees are really good at searching and comparing things.",
              "What are the methods for a Binary Search Tree and their Big O, time complexity?":"Binary Search Tree methods are:\n\t"
                                                                                                "1) lookup - O(log N) - Good/Excellent \n\t"
                                                                                                "2) insert - O(log N) - Good/Excellent \n\t"
                                                                                                "3) delete - O(log N) - Good/Excellent.",
              "In a perfect Binary Tree, how can we calculate the total number of nodes per level?":"The formula for calculating the total number of nodes is Level N: 2^N = Total no. Nodes\n\t"
                                                                                                    "i.e. Level 0: 2^0 = 1, Level 3: 2^3=8 - Total no. of nodes will always be even.",
              "What is the algorithm method or strategy used by Binary Search?":"Binary Search Tree uses the divide and conquer strategy to search for a value.\n\t"
                                                                                "It only searches subscripts and not the whole tree and all the values.",
              "What is unique of Binary Search Trees?":"Binary Search Trees can only be use with integer data values, not floats or strings",
              "What does BST withhold in their process?":"BST with holds relationships,(preserves relationships between node data values)",
              "What are rules of the BST?":"Rules of the BST are:\n\t"
                                           "1) Data Values to the right of the root/parent node it increases, if you go left it decreases\n\t"
                                           "2) BST child nodes and sub-child nodes can only have 2 childrens",
              "Define a unbalanced tree?":"One side of the tree may have single nodes (parent-child) many times,\n"
                                          "When a tree is unbalanced to one side using lookup,insert,and delete becomes O(n)\n",
              "What are the methods of an unbalanced tree and their time complexity, respectively?":"The methods or actions of an unbalanced tree are:\n\t"
                                                                                                    "1) lookup - O(n) -  Fair\n"
                                                                                                    "2) insert - O(n) - Fair\n"
                                                                                                    "3) delete - O(n) - Fair",
              "What type of functions can help balance an unbalance tree?":"AVL and Red Black Tree are functions that will help us balance and check trees.",
              "What are the pros of a Binary Search Tree?":"The pros for a BST are:\n\t"
                                                           "1) Better than O(n)\n\t"
                                                           "2) Ordered \n\t"
                                                           "3) Flexible Size - they can place a node anywhere in memory",
              "What are the cons of a Binary Search Tree?":"The cons for a BST are:\n\t"
                                                           "BST have no O(1) operations.",
              "What does a AVL Tree use?":"An AVL tree uses a type of rotation to balance out the tree.",
              "What does a Red Black Tree use?":"Red Black Trees automatically uses red black to balance the tree.",
              "Define a Heap Tree?":"A Heap is a special Tree-based data structure in which the tree is a complete binary tree.",
              "What are the two type of Heap Trees?":"The two type of Heap Trees are:\n\t"
                                                     "1) Max Heap - Root Node is the biggest, both childs are lower than the root.\n\t"
                                                     "2) Min Heap - Root Node is the smallest, both childs are higher than the root.",
              "What is the most-common use for Heap Trees?":"Heap Trees are most-commonly use in any algorithm where ordering is important..Priority Heaps.",
              "What are the method/actions of Trees and their time complexities?":"The methods & actions of Trees are:\n\t"
                                                                                  "1) lookup - O(n) - Fair\n"
                                                                                  "2) insert - O(log N) - Good/Excellent\n"
                                                                                  "3) delete - O(log N) - Good/Excellent",
              "How do Heap trees behave?":"Heaps add value in the tree from left to right and it'll bubble up.",
              "What are the pros of a Binary Heap?":"The pros of a binary heap tree are:\n\t"
                                                    "1) Better than O(n)\n"
                                                    "2) Priority\n"
                                                    "3) Flexible Size\n"
                                                    "4) Fast Insert",
              "What are the cons of Binary Heap?":"The cons of a binary heap tree are:\n\t"
                                                  "1) Slow lookup",
              "What do trie trees specialized in?":"Trie trees are used in searching mostly with text. (Called a prefix tree)",
              "What are the rules for a trie tree?":"The rules for a trie tree are:\n\t"
                                                    "1) empty root node, to start\n"
                                                    "2) children are usually letters\n"
                                                    "Some examples are auto completion, ip routing, search engines.\n"
                                                    "They have a Big O of O(length of word).",
              ""





}