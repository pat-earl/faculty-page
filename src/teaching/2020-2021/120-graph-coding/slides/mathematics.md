---
title: "Chapters 13 - Mathematics"
subtitle: "CSC120"
author: Patrick Earl
date: 04/15/2021
slideNumber: true
revealjstheme: robot-lung
width: 1600
height: 1000
transition: fade
---

## Mathematics
* Computers and Mathematics go together like peanut butter and jelly.
* You don't need to be a math wizard however, the computer does a lot of the hard work for you.
* You've done math just by using simple variables

```
avxspeed = avxspeed * -1;
ball_x = ball_x + avxspeed;
```
---

## Modulus
* Calculates the remainder when one number is divided by another.
* `20 modulo 6 equals 2 or 20 % 6 = 2`
* If *A* = *B* % *C*, *A* can never be larger than *C*.
* Modulo can be used to cycle a counter variable back to zero.

```
x = x + 1;
if(x >= limit) {
    x = 0;
}
// or 
x = (x + 1) % limit;
```

---

## Random Numbers
* **Example 13-2**

---

## Probability
* Given a system with a certain number of possible outcomes, the probability of any given event occurring is the number of of outcomes which qualify as that event divided by total number of possible outcomes.
* Using 52 card deck:
    * Drawing an ace: number of aces/number of cards = *4/27* = 0.077 = ~8%
    * Drawing a Diamond: *13/52* = 0.25 = 25%
* Probability in code
* **Example 13-3**


---

## Perlin Noise
* An Algorithm that generates "smooth" randomness. Which is useful in some cases. 
* `noise()`
    * Takes one argument, that controls the "time" of the noise. 
* Noise will always return a value between 0 and 1
* **Example 13-4**

```
float t = 0.0
void draw() {
    float noisevalue = noise(t);
    println(noise);

    // t += 0.01;
}
```

---

## *map*
* Commonly values are mapped to a range
    * Map the *mouseX* (0-*Width*) to a Color (0-255)
* map's arguments:
    * *value*: The value you want to map
    * *Current Min*: Minimum of value's range
    * *Current Max*: Maximum of value's range
    * *New Min*: The minimum of the new value's range
    * *New Max*: The maximum of the new value's range
    * *Returns* a new value
* Using map to control the background:

```
void setup() {
    size(640, 360);
}
void draw() {
    float r = map(mouseX, 0, width, 0, 255);
    float b = map(mouseY, 0, height, 255, 0); // Inverted mapping
}
```

--- 

## Angles
* Will continue with this next week.