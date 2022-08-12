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
              ""




}