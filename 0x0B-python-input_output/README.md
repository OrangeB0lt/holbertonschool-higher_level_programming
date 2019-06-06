# 0x0B. Python - Input/Output

## OBJECTIVES   
By the end of the project, be able to explain:   
   * files in Python:   
      * opening   
      * closing (and verifying closure)   
      * reading (both full content and line by line)    
      * writing   
   * JSON strings   
   * serialization and deserialization   

## REQUIREMENTS   

   * the first line of all files should be exactly `#!/usr/bin/python3`   
   * all code should use the `PEP8` style (version 1.7.*)   
   * all files must be executable   
   * all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)   
   * all modules should have documentation `python3 -c 'print(__import__("my_module").__doc__)'`   
   * all functions (inside and outside of classes) should have documentation `python3 -c 'print(__import__("my_module").my_function.__doc__)'`   

## EXERCISES   

### MANDATORY   

**[0-read_file.py](0-read_file.py)** - Write a function that reads a text file and prints it to stdout    
Prototype: ` def read_file(filename=""):`   

**[1-number_of_lines.py](1-number_of_lines.py)** - Write a function that returns the number of lines of a text file    
Prototype: `def number_of_lines(filename=""):`   

**[2-read_lines.py](2-read_lines.py)** - Write a function that reads `n` lines of a text file and prints it to stdout   
Prototype: `def read_lines(filename="", nb_lines=0):`   

**[3-write_file.py](3-write_file.py)** - Write a function that writes a string to a text file and returns the number of characters written   
Prototype: `def write_file(filename="", text=""):`   

**[4-append_write.py](4-append_write.py)** - Write a function that appends a string at the end of a text file and returns the number of characters added   
Prototype: `def append_write(filename="", text=""):`   

**[5-to_json_string.py](5-to_json_string.py)** - Write a function that returns the JSON representation of an object   
Prototype: `def to_json_string(my_obj):`   

**[6-from_json_string.py](6-from_json_string.py)** - Write a function that returns an object represented by a JSON string   
Prototype: `def from_json_string(my_str):`   

**[7-save_to_json_file.py](7-save_to_json_file.py)** - Write a function that writes an Object to a text file, using a JSON representation   
Prototype: `def save_to_json_file(my_obj, filename):`   

**[8-load_from_json_file.py](8-load_from_json_file.py)** - Write a function that creates an Object from a “JSON file”   
Prototype: `def load_from_json_file(filename):`   

**[9-add_item.py](9-add_item.py)** - Write a script that adds all arguments to a Python list, and then save them to a file named `add_item.json`   

**[10-class_to_json.py](10-class_to_json.py)** - Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object   
Prototype: `def class_to_json(obj):`   

**[11-student.py](11-student.py)** - Write a class `Student` that defines a student by:    
   * Public instance attributes:   
      * `first_name`   
      * `last_name`   
      * `age`   
   * Instantation with `def __init__(self, first_name, last_name, age):`   
   * Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance   

**[12-student.py](12-student.py)** - Write a class `Student` with all of the above and:   
   * Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance   
      * if `attrs` is a list of strings, only attributes name contain in this list must be retrieved   
      * otherwise, all attributes should be retrieved   

**[13-student.py](13-student.py)** - Write a class `Student` with all of the above and:   
   * Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instances   
      * `json` will always be a dictionary   
      * a dictionary key will be the public attribute name   
      * a dictionary value will be the value of the public attribute   

**[14-pascal_triangle.py](14-pascal_triangle.py)** - Write a function that returns a list of lists of integers representing the Pascal’s triangle of `n`   
Prototype: `def pascal_triangle(n):`   

### ADVANCED   

**[100-append_after.py](100-append_after.py)** - Write a function that inserts a line of text to a file, after each line containing a specific string   
Prototype: `def append_after(filename="", search_string="", new_string=""):`   

**[101-stats.py](101-stats.py)** - Write a script that reads `stdin` line by line and computes metrics:    
   * Input Format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`   
   * Each 10 lines and after every  keyboard interruption, print these statistics:   
      * Total file size `File size: <total size>` which is the sum of all previous file sizes   
      * Number of lines by status code:   
         * possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`    
	 * format: `<status code>: <number>`    
	 * if a status code doesn’t appear, don’t print anything for that code    

**[read_write_heap.py](read_write_heap.py)** - Write a script that finds a string in the heap of a running process, and replaces it   
Usage: `read_write_heap.py pid search_string replace_string`   
