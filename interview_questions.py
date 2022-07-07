int_quest_answ = {
    "What is Python?": [
        "Python is a high-level, interpreted, interactive and object-oriented scripting language.",
        "Python is designed to be highly readable and compatible with different platforms such as Mac, Window, Linux, Raspberry Pi, etc",
    ],
    "What type of language is Python": "Python is an interpreted languages, Interpreted language is any programming language that executes its statements line by line"
    "Programs written in Python run directly from the source code, with no intermediary compilation step.",
    "What is the difference between lists and tuples": [
        "Lists are mutable, Tuples are not",
        "List are usually slower than Tuples",
        "Lists are less reliable than Tuples,unexpected changes and errors",
        "Lists consume a lot of memory",
        "Lists consists of many built-in-functions, Tuples consist of none",
    ],
    "What is pep 8": "PEP in Python stands for Python Enhancement Proposal. It is a set of rules that specify how to write and design Python code for maximum readability.",
    "What are the 5 main Key features of Python": [
        "Python is an interpreted language, so it doesn't need to be compiled before execution, unlike languages such as C",
        "Python is dynamically typed, so there is no need to declare a variable with the data type.",
        "Python follows an object-oriented programming paradigm w/ exception to access specifiers.Python has classes,inheritance and "
        "all other OOPs concepts.",
        "Python is cross-platform language, i.e. run same on windows as in mac or linux",
        "Python is literally a general-purpose language, i.e., can be use in Data science, Machine Learning, web application",
    ],
    "How is Memory managed in Python": [
        "Memory in Python is managed by Python private heap space. All Python objects and data structures are located in a private heap. This"
        "private heap is taken care of by Python Interpreter itself, and a programmer doesn't have access to this private heap.",
        "Python memory manager takes care of the allocation of Python private heap space.",
        "Memory for Python private heap space is made available by Python's in-built garbage collector, which recycles and frees up all the unused memory.",
    ],
    "What is PYTHONPATH": "PYTHONPATH has a role similar to PATH. This variable tells Python Interpreter where to locate the module files imported into a program.Should include the Python "
    "source library directory and the directories containing Python source code.",
    "What are Python Modules": "Files containing Python codes are referred to as Python Modules. This code can either be classes,functions or variables. File with .py extension and contains an executable code. ",
    "What are python namespaces": [
        "A Python namespace ensures that object names in a program are unique and can be used without any conflict. Python implements these namespaces as dictionaries with 'name as key' mapped to object as value",
        "Local Namespace,within a function",
        "Global Namespace being use on ongoing project, created once",
        "Built-in Namespace, consists of built -in functions of core Python and "
        "dedicated built-in names for various types of exceptions",
    ],
    "Explain Inheritance in Python with an example": "As Python follows an object-oriented programming paradigm, classes in Python have the ability to inherit the properties of another class."
    "This process is known as inheritance. Inheritance provides the code reusability feature. The class that is being inherited is called a superclass"
    "or the parent class, and the class that inherits the superclass is called a derived or child class.",
    "What is scope resolution": "A scope is a block of code where an object in Python remains relevant. Local scope refers to the local objects included in the current function."
    "A global scope refers to the objects that are available throughout execution of the code. A module-level scope refers to the global objects that are associated with the"
    "current module in the program. Outermost scope refers to all the available built-in names callable in the program",
    "What is a dictionary in Python": "Python dictionary is one of the supported data types in Python. It is an unordered collection of elements. The elements in dictionaries are stored as key-value pairs."
    "Dictionaries are indexed by keys",
    "What are functions in Python?": "A function is a block of code which is executed only when a call is made to the function. def keyword is used to define a particular function.",
    "What is __init__ in Python": "Equivalent to constructors in OOP terminology, __init__ is a reserved method in Python classes. The __init__ method is called automatically whenever a new object is"
    "initiated.This method allocates memory to the new object as soon as it is created. This method can also be used to initialized variables",
    "What are the common built-in data types in Python": [
        "Number (immutable)",
        "String (immutable)",
        "Tuple (immutable)",
        "List (mutable)",
        "Dictionary (mutable)",
        "set (mutable)",
    ],
    "What are local variables and global variables in Python?": [
        "Local variable are any variable declared inside a function and it's accessibility remains inside the function only.",
        "Global variable are any variable declared outside te function and it can be easily accessible by any function present throughout the "
        "program.",
    ],
    "What is type conversion in Python?": [
        "Python provides you with a much-needed functionality of converting one form of data type into the needed one and this is known as type conversion.",
        "Implicit Type Conversion, in this form of type conversion python interpreter helps in automatically converting the data type into another data type without any"
        "User involvement",
        "Explicit Type Conversion, In this form of Type conversion the data type inn changed into a required type by the user.",
    ],
    "How to install Python on Windows and set a path variable?": [
        "Download and install Python (.exe)",
        "Remember location of where Python was installed;(cmd python on cmnd line)",
        "Open advance system settings and add a new variable and name it as PYTHON_NAME and paste the path from above",
        "Search for the path variable -> select its value and then select 'edi'",
        "Add a semicolon at the end of the value if it's not present and then type %PYTHON_HOME%",
    ],
    "What is the difference between Python Arrays and lists?": [
        "Lists consists of elements belonging to different data types. Array elements have same data type",
        "In lists no need to import module, need to explicit import module for array declaration",
        "Lists can have different types and sizes in nested. Array nested array must be same size",
        "Lists are recommended use for shorter sequence of data items,Arrays recommended for longer sequence",
        "Lists are more flexible for easy modification than arrays",
        "Arrays are comparatively more compact in memory size",
        "Lists can be printed entirely without loops",
    ],
    "Is python case sensitive": "Yes, Python is a case sensitive language. This means that Function and function both are different in python alike SQL and Pascal.",
    "What does [::-1] do": "[::-1] ,this is an example of slice notation and helps to reverse the sequence with the help of indexing.[Start,stop,step count]",
    "What are Python packages": "A Python package refers to the collection of different sub-packages and modules based on the similarities of the function.",
    "What are decorators in Python": "In Python, decorators are necessary functions that help add functionality to an existing function without changing the structure of the function at all."
    "These are represented by @decorator_name in Python and are called in a bottom-up format.\nExample:\n\t"
    "def decorator_lowercase(function):   # defining python decorator\n\t"
    "def wrapper():\n\t"
    "func = function()\n\t"
    "input_lowercase = func.lower\n\t"
    "return input_lowercase\n\t"
    "return wrapper\n\t"
    "@decorator_lowercase ##calling decorator\n\t"
    "def intro():               #Normal function\n\t"
    "return 'Hello, I AM SAM'\n\t"
    "hello()",
    "Is indentation required in Python": "Indentation in Python is compulsory and is part of its syntax.\n"
    "\nAll programming languages have some way of defining the scope and extent of the block of codes. In Python, it is indentation. "
    "Indentation provides better readability to the code, which is probably why Python has made it compulsory.",
    "How does break, continue and pass work": [
        "These statements help to change the phase of execution from the normal flow that is why they are termed loop control statements.",
        "Python break: This statement helps terminate the loop or the statement and pass the control to the next statement",
        "Python continue: This statement helps force the execution of the next iteration when a specific condition meets, instead of terminating it.",
        "Python pass: This statement helps write the code syntactically and wants to skip the execution. It is also considered a null operation as nothing happens"
        "when you execute the pass statement.",
    ],
    "How can you randomize the items of a list in place in Python": "By using Shuffle() function from the random library.",
    "How to comment with multiple lines in Python?": "Lines or statements need to prefixed by #",
    "What type of language is python?Programming or scripting?": "Generally, Python is an all purpose Programming Language, in addition to that Python is also capable of performing scripting.",
    "What are negative indexes and why are they used?": "to access an element from ordered sequences, we simply use the index of the element, which is the position number of that particular element."
    "starts 0 and goes forward, negatives help index from rear -1 and goes up in negatives til reach the [0] comparative index.",
    "Explain split(),sub(),subn() methods of 're' module in Python?": [
        "These methods are used to modify strings",
        "split(): This method is used to split a given string into a list",
        "sub(): This method is used to find a substring where a regex pattern matches, and then it replaces the matched substring with a different string",
        "subn(): This method is similar to sub() method, but it returns the new string, along with the number of replacements",
    ],
    "What do you mean by Python literals?": [
        "Literals refer to the data which will be provided to a given in a variable or constant",
        "String Literals:\n\t"
        "These literals are formed by enclosing text in the single or double quotes",
        "Numeric Literals:\n\t"
        "Python numeric literals support three types of literals\n\t"
        "Integer,Float,Complex  '1.73j'",
        "Boolean Literals:\n\t"
        "Boolean literals help to denote boolean values. It contains either True or False.",
    ],
    "What is a map function in Python?": "The map() function in Python has two parameters, function and iterable. The map() function takes a function as an argument and then applies that function"
    "to all the elements of an iterable, passed to it as another argument it returns an object list of results.\nFor example:"
    "\n\tdef calculateSq(n):\n\t"
    "return n*n\n\t"
    "numbers = (2,3,4,5)\n\t"
    "result = map(calculateSq,numbers)\n\t"
    "print(result)",
    "What are the generators in python?": "Generator refers to the function that returns an iterable set of items",
    "What are python iterators": "These are the certain objects that are easily traversed and iterated when needed.",
    "Do we need to declare variables with data types in Python": "No. Python is a dynamically typed language, I.E., Python Interpreter automatically identifies the data type of a variable based on the type of value"
    "assigned to the variable.",
    "What are Dict and List comprehensions? - Fix": "Python comprehensions are like decorators, that help to build altered and filtered lists, dictionaries, or sets from a given list, dictionary or set."
    "Comprehension saves a lot of time and code that might be considerably more complex and time-consuming\n"
    "Comprehensions are beneficial in the following scenarios:"
    "\n\tPerforming mathematical operations on the entire list\n\t"
    "Performing conditional filtering operations on the entire list \n\t"
    "Combing multiple lists into one \n\t"
    "Flattening a multi-dimensional list\n\t"
    "For Example:\n\t\t"
    "my_list =[2,3,5,7,11]\n\t\t"
    "squared_list = [x**2 for x in my_list]  # list comprehension\n\t\t"
    "#output => [4,9,25,49,121]\n\t\t"
    "squared_dict = {x:x**2 for x in my_list} # Dict comprehension\n\t\t"
    "#output => {11:121,2:4,3:9,5:25,7:49}",
    "How do you write comments in python?": "Python comments are the statement used by the programmer to increase the readability of the code.Use # and strings enclosed with triple quotes",
    "Is multiple inheritance supported in Python?": "Yes, unlike Java, Python provides users with a wide range of support in terms of inheritance and its usage. Multiple inheritance refers to"
    "a scenario where a class is instantiated from more than one individual parent class. This provides a lot of functionality and "
    "advantages to users.",
    "What is the difference between range & xrange?": [
        "Functions in Python, range() and rangex() are used to iterate in a loop for a fixed number of times. "
        "Functionality-wise, bot these functions are the same. The difference comes when talking about Python version support for these functions and their return values.",
        "In python3 xrange is not supported and superseded by range()",
    ],
    "What is pickling and unpickling?": "The Pickle module accepts the Python object and converts it into a string representation and stores it into a file by using the dump function."
    "This process is called pickling. On the other hand, the process of retrieving the original Python objects from the string representation is called unpickling.",
    "What do you understand by Tkinter": "Tkinter is a built-in Python module that is used to create GUI applications. It is Python's standard toolkit for GUI development. Tkinter comes with Python,"
    "so there is no separate installation needed. You can start using it by importing it in your script",
    "Is Python fully object oriented?": "Python does follow an object-oriented programming paradigm and has all the basic OOPs concepts such as inheritance,polymorphism, and more, with the exception"
    " of access specifiers. Python doesn't support strong encapsulation (adding a private keyword before data members). Although, it has a convention "
    "that can be used for data hiding, i.e, prefixing a data member with two underscores.",
    "Differentiate between NumPy and SciPy": [
        "NumPy stands for Numerical Python, SciPy stands for Scientific Python",
        "NumPy is used for efficient and general numeric computations on numerical data saved in "
        "arrays.While SciPy module is a collection of tools in Python used to perform operations "
        "such as integration, differentiation, and more.",
        "Full-fledged algebraic functions are available in SciPy for algebraic computations.",
    ],
    "Explain all file processing modes supported in Python": [
        "Python has various file processing modes.",
        "For opening files, there are three modes:\n\t"
        "read-only mode (r)\n\t"
        "write-only mode (w)\n\t"
        "read-write mode (rw)\n"
        "For opening a text files using the above modes, we will have to append 't' with them as follows:\n\t"
        "read-only mode (rt)\n\t"
        "write-only mode (wt)\n\t"
        "read-write mode (rwt)\n"
        "Similarly, a binary file can be opened by appending 'b' with them as follows:\n\t"
        "(rb)\n\t(wb)\n\t(rwb)\n"
        "To append the content in the files, we can use the append mode (a):"
        "\n\tFor text files, the mode would be 'at'\n\t"
        "For binary files, it wold be 'ab'",
    ],
    "What do file-related modules in Python do? Name some?": "Python comes with some file-related modules that have functions to manipulate text files and binary files in a file system."
    "These modules can be used to create text or binary files, update their content, copy, delete, and more.\n\n"
    "Some file-related modules are oos, os.path, and shutil.os. the os.path module has functions to access the file system, while the "
    "shutil.os module can be used to copy or delete files.",
    "Explain the use of the 'with' statement and its syntax?": "In Python, using the 'with' statement, we can open a file and close it as soon as the block of code, where 'with' is used, exits. In this way, we can opt for not using the close() method."
    "\n\tExample:\n\t with open('filename','mode') as file_var:",
    "Write a code to display the contents of a file in reverse?": "Code:\n\t"
    "for line in reversed(list(open(filename.txt):"
    "\n\t\t print(line.rstrip())",
    "Which of the following is an invalid Statement?\n\t1) xyz=1,000,000\n\t2) x y z=1000,2000,3000\n\t3) x,y,z=1000,2000,3000\n\t4)x_y_z =1,000,000": "Answer is 2) x y z= 1000,2000,3000 is invalid.",
    "Write a command to open the file c:\hello.txt for writing?": "f = open('hello.txt','wt')",
    "What does len() do?": "len() is an inbuilt function used to calculate the length of sequences like list, python string, and array.",
    "What does *args and **kwargs mean?": ".*args: It is used to pass multiple arguments in a function.\n**kwargs: It is used to pass multiple keyworded arguments in a function in python.",
    "How will you remove duplicate elements from a list?": "To remove duplicate elements from the list we use the set() function.",
    "How can files be deleted in Python?": "Import OS Module and use os.remove() function for deleting a file in python.",
    "How will you read a random line in a file?": "We can read a random line in a file using the random module: \n\t import random\n\t def read_random(fname):\n\t\t"
    "lines= open(fname).read().splitlines()\n\t\t"
    "return random.choice(lines)\n\t"
    "print(read_random('hello.txt')",
    "Write a Python program to count the total number of lines in a text file?": "def file_count(fname):\n\t"
    "with open(fname) as f:\n\t"
    "\t for i, 1 in enumerate(f):"
    "\n\t\tpass\n\t"
    "return i+1\n"
    "print('total number of lines in the text file:' , file_count('file.txt'))",
    "What would be the output if I run the following code block?\n"
    "list1 = [2,33,222,14,25]\n"
    "print(list1[-2]": "Output: 14",
    "What is the purpose of is, not and in operators?": "Operators are referred to as special functions that take one or more values(operands) and produce a corresponding result.\n\t"
    "is: returns the true value when both the operands are true (Example:'x' is 'x')\n\t"
    "not: return the inverse of the boolean value based upon the operands\n\t"
    "in: helps to check if the element is present in a given Sequence or not",
    "Whenever Python exits, why isn't all the memory de-allocated?": "Whenever Python exits, especially those Python modules which are having circular references to other objects or the objects"
    "that are referenced from the global namespaces are not always de-allocated or freed.\n"
    "IIt is not possible to de-allocate those portions of memory that are reserved by the C library.\n"
    "On exit, because of having its own efficient clean up mechanism, Python would try to de-allocated every object.",
    "How can the ternary operators be used in python?": "The ternary operator is the operator that is used to show conditional statements in Python. \n\tSyntax:\n\t\t"
    "[on_tru] if [expression] else [on_false]x, y = 10, 20 count = x if x < y else y",
    "How to add values to a python array?": "In python, adding elements in an array can be easily done with the help of extend(), append(), and insert() functions.\n\t"
    "Consider the following example:\n\t"
    "x=arr.array('d',[11.1,2.1,3.1])\n\t"
    "x.append(10.1)\n\t"
    "print(x) #[11.1,2.1,3.1,10.1]\n\t"
    "x.extend([8.3,1.3,5.3])\n\t"
    "print(x) #[11.1,2.1,3.1,10.1]\n\t"
    "x.insert(2,6.2)\n\t"
    "print(x) #[11.1,2.1,6.2,3.1,5.3]",
    "How to remove values to a python array?": "Elements can be removed from the python array using pop() or remove() methods,\n"
    "pop():This function will return the removed element.\n"
    "remove():will not return the removed element.",
    "Write a code to sort a numerical list in Python?": "The following code can be used to sort a numerical list in Python:\n\t"
    "list = ['2,'3','4']\n\t"
    "list = [int(i) for i in list]\n\t"
    "print(list.sort())",
    "Can you write an efficient code to count the number of capital letters in a file?": "The normal solution for this problem statement would be as follows:\n\t"
    "with open(SOME_LARGE_FILE) as countletter:\n\t"
    "count = 0\n\t"
    "text = countletter.read()\n\t"
    "for character in text:\n\t"
    "if character.isupper():\n\t"
    "count += 1\n\t"
    "\n #or\n\t"
    "count sum(1 for line in countletter for character in line if character.isupper())",
    "How will you reverse a list in Python?": "The function list.reverse() reverses the objects of a list.",
    "How will you remove the last object from a list in Python?": "list.pop(obj=list[-1]:\n",
    "How can you generate random numbers in Python": "This achieved with importing the random module, it is the module that is used to generate random numbers.",
    "How will you convert a string to all lowercase?": "lower() function is used to convert a string to lower case",
    "Why would you use NumPy arrays instead of lists in Python": "NumPy arrays provide users with three main advantages as shown below:\n\t"
    "1) NumPy arrays consume a lot less memory, thereby making code more efficient\n\t"
    "2) NumPy arrays execute faster and do not add heavy processing to the runtime.\n\t"
    "3) NumPy has a highly readable syntax, making it easy and convenient for programmers.",
    "what is Polymorphism in Python": "Polymorphism is the ability of the code to take multiple forms. Let's say, if the parent class has a method named XYZ then the child class can also have a method"
    "with the same name XYZ having its own variables and parameters.",
    "Define encapsulation in Python": "encapsulation in Python refers to the process of wrapping up the variables and different functions into a single entity or capsule."
    "Python class is the best example of encapsulation in python.",
    "What advantages do NumPy arrays offer over (nested) Python List?": "Nested Lists:\n\t"
    "Python lists are efficient general-purpose containers that support efficient operations like insertion, appending, deletion and"
    "concatenation.\n\t"
    "The limitations of lists are that they don't support 'vectorized' operations like element wise addition and multiplication, and the fact that they"
    "can contain objects of differing types means that Python must store type information for every element, and must execute type dispatching code when "
    "operating on each element.\n"
    "NumPy:\n\t"
    "NumPy is more efficient and more convenient as you get alot of vector and matrix operations for free, which helps avoid unnecessary work and complexity"
    "of the code. Numpy is also efficiently implemented when compared to nested\n\t"
    "NumPy array is faster and contains a lot of built-in functions which will help FFTs, convolutions, fast searching, linear algebra, basic statistics, histograms,etc.",
    "What is the lambda function in Python?": "A lambda function is an anonymous function ( a function that does not have a name ) in Python. To define anonymous functions, we use the 'lambda' keyword instead of"
    "the 'def' keyword, hence the name 'lambda function'. Lambda functions can have any  number of arguments but only one statement.\n"
    "For example:\n\t"
    "a = lambda x,y : x*y\n\t"
    "print(a(5,6))\n\t"
    "#output: 30",
    "What is self in Python?": "Self is an object or an instance of a class. This is explicitly included as the first parameter in Python. On the other hand, in Java it is optional."
    "It helps differentiate between the methods and attributes of a class with local variables.\nSyntax:\n\t"
    "Class A:\n\t\t"
    "def func(self):\n\t\t"
    "print('hi')",
    "What is the difference between append() and extend() methods?": "Both append() and extend() methods are methods used to add elements at the end of a list.\n\t"
    "append(element): ADDs the given element at the end of the list that called this append() method.\n\t"
    "extend(another-list): ADDs the elements of another list at the end of the list that called this extend() method",
    "How does Python Flask handle database requests?": "Flask supports a database-powered application (RDBS). Such a system requires creating a schema, which needs piping the schema.sql file into the"
    "sqlite3 command. Python developers need to install the sqlite3 command to create or initiate the database in Flask.\n"
    "Flask allows to request for a database in three ways:\n\t"
    "before_request(): They are called before a request and pass no arguments\n\t"
    "after_request(): They are called after a request and pass the response that will be sent to the client.\n\t"
    "teardown_request(): They are called in a situation when an exception is raised and responses are not guranteed."
    "They are called after the response has been constructed. They are not allowed to modify the request, and their values are ignored.",
    "What is docstring in Python?": "Python lets users include a description (or quick notes) for their methods using documentation strings or docstrings. Docstrings are different from regular comments"
    "in Python as rather than being completely ignored by the Python Interpreter like in the case of comments, these are defined within triple quotes.",
    "How is Multithreading achieved in Python?": "Python has a multi-threading package, but commonly not considered as good practice to use it as it will result in increased code execution time.\n\t"
    "Python has a constructor called the Global Interpreter Lock (GIL). The GIL ensures that only one of your 'threads' can execute at one time."
    "The process  makes sure that a thread acquires the GIL, does a little work, then passes the GIL onto the next thread.\n\n\t"
    "This happens at a ver Quick instance of time and that's why to the human eye it seems like your threads are executing parallely, but in reality they are"
    "executing one by one by just taking turns using the same CPU core.",
    "What is slicing in Python?": "Slicing is a process used to select a range of elements from sequence data like list, string and tuple."
    "Slicing is beneficial and easy to extract out the elements. It requires a : (colon) which separates the start index and end index of the field. All the data sequence"
    "types List or typle allows us to use slicing to get the needed elements. Although we can get elements by specifying an index, we get only a single element"
    "whereas using slicing we can get a group or appropriate range of needed elements. Example: List_names[start:stop]",
    "What is functional programming? Does Python follow a functional programming style? ": "Functional programming is a coding style where the main source of logic in a program comes from functions.\n\n"
    "Incorporating functional programming in ou codes means writing pure functions.\n\n"
    "Pure functions are functions that cause little or no changes outside the scope of the function. These"
    "changes are referred to as side effects. To reduce side effects, pure functions are used, which makes the"
    "code easy-to-follow, test, or debug.\n\n",
    "Which one of the following is not the correct syntax for creating a set in Python?\n\t"
    "1) set([[1,2],[3,4],[4,5]])\n\t"
    "2) set([1,2,2,3,4,5])\n\t"
    "3) {1,2,3,4}\n\t"
    "4) set((1,2,3,4))": "Ans: 1  is not the correct way.",
    "What is monkey patching in Python?": "Monkey patching is the term used to denote the modifications that are done to a class or a module"
    "during the runtime. This can  only be done as Python supports changes in the behavior of the program while being executed.\n\n",
    "What is the difference between / and // operator in Python?": "/ is a division operator and return quotient value\n\n"
    "// is know as floor division operator and used to return only the value of quotient before decimal.",
    "What is pandas?": "Pandas is an open source python library which supports data structures for data based operations associated with data analyzing and data Manipulation. Pandas with its"
    "rich sets of features fits in every role of datta operation, whether it be related to implementing different algorithms or for solving complex business problems. "
    "Pandas helps to deal with a number of files in performing certain operations on the data stored by files.",
    "What are dataframes?": "A dataframe refers to a two dimensional mutable data structure or data aligned in the tabular form with labeled axes(rows and columns)\n"
    "Syntax:\n\t"
    "pandas.DataFrame(data,index,columns,dtype)\n"
    "data: refers to various forms like ndarray, series, map, lists, dict, constants and can take other Data-Frame as Input.\n"
    "index: This argument is optional as the index for row labels will be automatically taken care of by pandas library.\n"
    "columns: this argument is optional as the index for column labels will be automatically taken care of by pandas library.\n"
    "Dtype: refers to the data type of each column",
    "How to combine dataframes in Pandas": "The different dataframes can be easily combined with the help of functions listed: \n"
    "\tappend(): This function is used for horizontal stacking of dataframes. \n\t\t"
    "data_frames1.append(data_frame2)\n\t"
    "concat(): This function is used for vertical stacking and best suites when the dataframes to be combined possess the same column and similar fields.\n\t\t"
    "pd.contact([data_frame1,data_frame2])"
    "join(): This function is used to extract data from different dataframes which have one or more columns common.\n\t\n"
    "data_frame1.join(data_frame2)",
    "How do you identify missing values and deal with missing values in Dataframe?": "Identification: isnull() and isna() functions are used to identify the missing values in your data loaded into dataframe."
    "\n\t missing_count = data_frame1.isnull.sum()\n"
    "Handling missing Values: there are two ways of handling missing values:\n\t"
    "Replace the missing values with 0\n\t\t"
    "df['col_name'].fillna0\n\t"
    "Replace the missing values with the mean value of that column\n\t\t"
    "df['col_name'] = df['col_name'].fillna((df['col_name'].mean()))",
    "What is regression?": "Regression is termed as supervised machine learning algorithm technique which is used to"
    "find the correlation between variables and help to predict the dependent variable(y) based upon the independent variable (x). It is mainly used for prediction,"
    "time series modeling, forecasting, and determining the casual-effect relationship between variables.\n"
    "Scikit library is used in python to implement the regression and all machine learning algorithms\n"
    "Linear regression: used when the variables are continuous and numeric in nature\n"
    "Logistic Regression: Used when the variables are continuous and categorical in nature",
    "What is classification?": "Classification refers to a predictive modeling process where a class label is predicted for a given example of input data. It helps categorize the provided input into a "
    "label that other observations with similar features have. For example, it can be used for classifying a mail whether it is spam or not, or for checking"
    "whether users will churn or not based on their behavior \n"
    "These are some of the classification algorithms used in Machine Learning:\n\t"
    "Decision tree\n\t"
    "Random forest classifier\n\t"
    "Support vector machine\n\t",
    "How do you split the data in train and test dataset in python?": "This can be achieved by using the scikit machine learning library and importing train_test_split function "
    "in python",
    "What is SVM?": "Support vector machine (SVM) is a supervised machine learning model that considers the classification algorithms for two-group classification problems. "
    "Support vector machine is a representation of the training data as points in space are separated into categories with the help of a clear gap that should be as wide as possible.",
    "Write a code to get the indices of N maximum values from a NumPy array?": "We can get the indices of N maximum values from a NumPy array using the below code:\n\t"
    "import numpy as np\n\t"
    "ar = np.array([1,3,2,4,5,6])\n\t"
    "print(ar.argsort()[-3:][::-1]",
    "What is the easiest way to calculate percentiles when using Python?": "The easiest and the most efficient way you can calculate percentiles in Python is to make use of NumPy arrays and its functions.\n"
    "Consider the following example:\n\t"
    "import numpy as np\n\t"
    "a = np.array([1,2,3,4,5,6,7])\n\t"
    "p = np.percentile(a,50)\n\t"
    "print(p)",
    "Write a Python program to check whether a given string is a palindrome or not, without using an iterative method": "A palindrome is a word, phrase or sequence that reads the same backwards as forwars.\n\t"
    "def fun(string):\n\t"
    "s1 = string\n\t"
    "s = string[::-1]\n\t"
    "if (s1==s):\n\t"
    "return true \n\t"
    "else: \n\t"
    "return false \n\t"
    "print(fun('madam'))",
    "Write a Python program to calculate the sum of a list of numbers?": "def sum(num):\n\t"
    "if len(num) == 1\n\t"
    "return num[0]\n"
    "\telse:\n\t"
    "return num[0]+ sum(num[1:])\n\t"
    "print(sum([2,4,5,6,7])",
    "Write a program Program to print ASCII Value of a character in python": "x ='a' \n print(ord(x))",
}
