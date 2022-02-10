---
marp: true
theme: gaia
_class:
  - lead
paginate: true
backgroundColor: #fff
---

# **Data Science File Formats**

CSC223 - Advanced Scientific Programming

Prof. Patrick Earl

Spring 2022

---

# **Comma Separated Values** (CSV)

- Delimited Text File, Commas are used to separate values.
- There is no set standard for how CSVs should be formatted
    - Therefore you can experience different "dialects"
- Typical Format:
    - **First Line**: Header Fields - Names of the columns 
    - Every line that follows is an individual record of that data.

---

# Python `csv` module

- Provides access to functions to easily read & write CSV (or similar Tabular Data) files.
- `csv.reader`
    - Takes a file like object
    - Can be iterated through to generate a tuple of each line

---

# Reading a csv
```python
import csv

f = open('stats.csv')
reader = csv.reader(f)

for line in reader:
    print(line)
```

---

# Writing a CSV

```python
import csv

headers = ['Name', 'Level', 'Salary']

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    # Output the header line
    writer.writerow(headers)
    writer.writerow(['Joe Bob', 'Associate', 55000])
```

---

# Reader/Writer Arguments

<style scoped>
table, p {
    font-size: 75%
}
</style>

The reader and writer can be modified to handle different flavors. See documentation for a full listing and explanation. 

| Argument | Description |
| -------- | ----------- |
| delimiter | One-character string to separate fields (Default is `,`) |
| lineterminator | How a line should be terminated. `\n` for UNIX files, `\r\n` for Windows |
| quotechar | Quote characters for fields with special characters (to escape) |
| qouting | What quoting convention to use |

---

# **JSON Files**

- JavaScript Object Notation
- Provides a more flexible tabular text format than CSVs
- Data follows a `key:value` pairing
- Python provides an almost 1:1 mapping to a *dictionary*
    - Python doesn't accept the "null" type.

---

# Example JSON

```json
{
    "name": "Patrick",
    "home_country": "United States",
    "pets": [
        {
            "type": "cat",
            "name": "Roger"
        }
    ],
    "siblings": [
        {"name": "Emily", "pets": null},
        {"name": "Joey", "pets": null},
        {"name": "Colin", "pets": null},
    ]
}
```

---

# Python Data Types

- String
- Number
- Object (Another JSON Object)
- Array (List)
- Boolean
- Null

- *Keys* must always be a string

---

# Python's `json` module

- Provides functionality for reading or writing JSON files
- JSON can be written to a file or encoded as a string
- Same with reading

---

# Reading a JSON File

```python
import json

with open('results.json`) as f:
    data = json.load(f)

print(data)
print(type(data))
```

---

# Writing a JSON File

```python
import json

f = open("results.json", "w") 

# Dumps the value stored in data to the file object 'f'
json.dump(data, f)
f.close()
```