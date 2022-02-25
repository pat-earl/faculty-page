title: Homework #3

## Data Formats

**Due:**
: Friday, March 4th

**Purpose:**
: Usage of Python Standard Library Modules
: Understanding of the CSV and JSON file formats

## Description

You are to use the file named `netflix_titles.csv` which is from the [Netflix Movies and TV Shows](https://www.kaggle.com/shivamb/netflix-shows)
dataset hosted on Kaggle. This file will be converted from the CSV file format into JSON.

The file can be downloaded here: [[materials/netflix_titles.csv]]

Your program will complete the following data processing steps:

1. Read the data using the Python *CSV* library.
2. Retrieve the subset of content that have "TV Show" in the type field.
3. From this subset, keep the following fields: "show_id", "title", "director", "country", 
"date_added", "duration".
4. Sort the shows in descending order based on the number of seasons (*Duration* field).
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
Your JSON file should be formatted properly, meaning that
all the data is on separate lines as seen in the example output below.

You may hard-code the filename in your program. Meaning, the program is only intended to work
with the supplied dataset. Your json file can be named anything, but must have a `.json` file extension.

*Other Information/Requirements:*
: The order of the keys in *each* dictionary isn't important. The order of the objects in the overall output needs to be as specified.
: You **can only use** the `csv` and `json` python libraries. 
: Your program must use functions.
: The format of the "date_added" date doesn't matter. 

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
    * 10 points - Correct field names
    * 10 points - Correct field values
    * 10 points - Sorted by "duration" field
    * 10 points - All "TV Shows" fields
    * 5 points - Output is formatted as shown in the example output

## Example Output

A small subset of the overall output file.

```
[
    ...
    {
        "show_id": "s3839",
        "title": "Mad Men",
        "director": "",
        "country": "United States",
        "date_added": " March 22, 2015",
        "duration": "7 Seasons"
    },
    {
        "show_id": "s3963",
        "title": "Marvel's Agents of S.H.I.E.L.D.",
        "director": "",
        "country": "United States",
        "date_added": "October 30, 2020",
        "duration": "7 Seasons"
    },
    ...
]
```