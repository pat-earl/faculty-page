---
title: "Chapters 15 - Images"
subtitle: "CSC120"
author: Patrick Earl
date: 04/15/2021
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: fade
---

## Working with images

* `PImage` is similar to working with a user-defined class.
* Stored in a variable named `img` of type `PImage`.
    * `loadImage()` loads the image and creates a new instance of `PImage`
* `createImage()` can be used to create a blank image 
    * This process is slow and should be done once (Like in setup)
* Use the `image` function to actually display it

---

## Image Animation 
* **Example 15-2**

---

## Image Filters
* Processing provides the ability to change the brightness, transparency, etc.
* `tint()`
  
---

## Arrays of Images
* You could have a different background whenever a user clicks the mouse. 
* Arrays would be a great storage method for having multiple images, however it does become a bit clunky.

```
PImage[] images = new PImage[5];

images[0] = loadImage("cat.jpg");
images[1] = loadImage("mouse.jpg");
images[2] = loadImage("dog.jpg");
images[3] = loadImage("kangaroo.jpg");
images[4] = loadImage("porcupine.jpg");
```

---

* Another option is to define the files in an array of Strings:

```
String[] filenames = {"cat.jpg", "mouse.jpg", "dog.jpg", "kangaroo.jpg"};

for (int i = 0; i < filenames.length; i++) {
    images[i] = loadImage(filenames[i])
}
```

---

* Or, name the files a common name + an integer.
    * Like "animal1.jpg", "animal2.jpg"
* **Example 15-3**
* **Example 15-4**

---

## Pixels
* The many functions used to draw shapes are only one part of the process. They are using code written by others to change the colors of a particular pixel on the display. 
* Processing provides the `pixels` array which allows the user to directly manipulate the underlying pixels.
* Pixels are stored in a one dimensional or linear sequence, even though we think of them on a 2D plane. 
* You have to follow this flow when attempting to change the `pixels` array.
    * `loadPixels()`
    * Do stuff to them
    * `updatePixels()`
* What index do you want? Use this formula:
    * `x + y * width`
* **Example 15-6**

## Image Pixels
* Processing also provides the capability to change pixels in an Image as well.
* **Example 15-7**

---

## Image Processing
* **Example 15-8**