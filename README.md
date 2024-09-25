
# Python Data Structures: List, Dictionary, and Set Operations

## 📚 Introduction

Welcome to the **Python Data Structures** repository! This project is designed for MCA students and beginners who are eager to learn how to work with Python's fundamental data structures: **lists**, **dictionaries**, and **sets**. Through this simple script, you'll understand how to create these data structures and perform basic operations such as adding, removing, and modifying elements.

## 🚀 Features

- **List Operations**
  - Create a list
  - Add elements
  - Remove elements
  - Modify elements

- **Dictionary Operations**
  - Create a dictionary
  - Add key-value pairs
  - Remove key-value pairs
  - Modify values

- **Set Operations**
  - Create a set
  - Add elements
  - Remove elements
  - Handle duplicates

## 🛠️ Prerequisites

Before you get started, ensure you have the following installed on your machine:

- **Python 3.x**: You can download it from the [official Python website](https://www.python.org/downloads/).

## 📥 Installation

1. **Clone the Repository**

   Open your terminal or command prompt and run:

   ```bash
   git clone https://github.com/anuj-cmyk/python-data-structures.git
   ```

   

2. **Navigate to the Project Directory**

   ```bash
   cd python-data-structures
   ```

## 📝 Usage

1. **Run the Python Script**

   Execute the script using Python:

   ```bash
   python data_structures.py
    

## 📖 Script Overview

The `data_structures.py` script performs the following operations:

### 1. List Operations

- **Create a List**

  ```
  my_list = [1, 2, 3]
  ```

- **Add an Element**

  ```
  my_list.append(4)
  ```

- **Remove an Element**

  ```
  my_list.remove(2)
  ```

- **Modify an Element**

  ```
  my_list[1] = 5
  ```

### 2. Dictionary Operations

- **Create a Dictionary**

  ```
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  ```

- **Add a Key-Value Pair**

  ```
  my_dict['d'] = 4
  ```

- **Remove a Key-Value Pair**

  ```
  del my_dict['b']
  ```

- **Modify a Value**

  ```
  my_dict['a'] = 10
  ```

### 3. Set Operations

- **Create a Set**

  ```
  my_set = {1, 2, 3}
  ```

- **Add an Element**

  ```
  my_set.add(4)
  ```

- **Remove an Element**

  ```
  my_set.remove(2)
  ```

- **Attempt to Add a Duplicate**

  ```
  my_set.add(3)
  ```

### 4. Final Output

The script prints the state of the list, dictionary, and set after each operation, providing a clear view of how each data structure changes over time.

## 📊 Sample Output

When you run the script, you should see the following output:

```
List after adding 4: [1, 2, 3, 4]
List after removing 2: [1, 3, 4]
List after modifying second element to 5: [1, 5, 4]

Dictionary after adding key 'd' with value 4: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Dictionary after removing key 'b': {'a': 1, 'c': 3, 'd': 4}
Dictionary after modifying value of key 'a' to 10: {'a': 10, 'c': 3, 'd': 4}

Set after adding 4: {1, 2, 3, 4}
Set after removing 2: {1, 3, 4}
Set after trying to add duplicate 3: {1, 3, 4}

Final List: [1, 5, 4]
Final Dictionary: {'a': 10, 'c': 3, 'd': 4}
Final Set: {1, 3, 4}
```

## 🧠 Explanation

### 🗒️ Lists

- **Adding Elements**: Use `.append()` to add an element to the end of the list.
- **Removing Elements**: Use `.remove()` to remove the first occurrence of a specified value.
- **Modifying Elements**: Access elements by their index and assign a new value.

### 📖 Dictionaries

- **Adding Key-Value Pairs**: Assign a value to a new key directly.
- **Removing Key-Value Pairs**: Use `del` followed by the key to remove the pair.
- **Modifying Values**: Assign a new value to an existing key.

### 🛍️ Sets

- **Adding Elements**: Use `.add()` to include a new element.
- **Removing Elements**: Use `.remove()` to delete a specific element.
- **Handling Duplicates**: Sets automatically ignore duplicate additions, ensuring all elements are unique.

## 🤝 Contributing

Contributions are welcome! If you have suggestions, improvements, or find any issues, feel free to open an [issue](https://github.com/anuj-cmyk/python-data-structures/issues) or submit a [pull request](https://github.com/anuj-cmyk/python-data-structures/pulls).


## 💡 Acknowledgements

- Inspired by educational needs for understanding Python data structures.
- Thanks to the Python community for continuous support and resources.
