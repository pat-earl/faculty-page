title: Homework #3

<br>

## Data Formats

**Due**
: Sunday Feb 28, 2021

Assignment Purpose:

* Extracting information from one file format and write it out as another

## Description

You are to use the file named `netflix_content.csv` which was adopted from [Netflix Movies and TV Shows](https://www.kaggle.com/shivamb/netflix-shows)
hosted on Kaggle. You'll be converting this file to the *JSON* data format, extracting a small
subset of the information found within it.

These are the data processing steps:

1. Read the data using the Python *CSV* library.
2. Retrieve the subset of content that have "TV Show" as the type.
3. From this subset, keep the following fields: "show_id", "title", "director", "country", 
"date_added", "duration".
4. Sort the shows based on alphabetic order of the "title" field.
5. Write the data to a JSON file using the Python *JSON* library.

The output must have the following format for each show:

```
{
    "show_id": id,
    "title": title,
    "director": director,
    "country": country,
    "date_added": date_added,
    "duration": duration
}
```

The values for each key should be replaced with the respective data. Each show should be it's own
JSON object in the output file.

You may hard-code the filename in your program. Meaning, the program is only intended to work
with the supplied dataset.

## Submission

Turn in a file named `main.py`, in the correct D2L assignment folder. Any other file name will not
be accepted.

## Grading Criteria

*NOTE: If your code fails to run on the Python3 interpreter, it will result in an automatic zero
for this assignment*

Assignment is worth 100 points

* 10 Points - proper Python module conventions
* 15 Points - Thoughtful and Purposeful Code Documentation
* 20 Points - correct use of Python libraries 
  * 10 points - *json* library
  * 10 points - *csv* library
* 55 Points - correct output
  * 10 points - Output is in JSON format
  * 10 points - Correct field order
  * 10 points - Correct field values
  * 10 points - Sorted by "title" field
  * 15 points - All "TV Shows" fields
