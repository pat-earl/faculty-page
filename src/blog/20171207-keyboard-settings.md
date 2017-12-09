title: Swapping control/caps lock, and using Apple keyboards on Linux
summary: I rarely use caps lock and often use control. Since the caps lock key is located on the home row, I find typing more efficient if I swap control and the left caps lock. I also like to swap the `command` and `option` modifiers when I use Apple keyboards, and make the funciton keys work without having to use the `FN` modifier. Here are instructions on each of these.

{{summary}}

## Swapping control and caps lock

To swap control and caps lock for your current session, type:

    setxkbmap -option ctrl:swapcaps

To make it permanent, put it in your `~/.xinitrc`. Alternately, if you have root access, then edit `/etc/default/keyboard` and add:

``` shell
XKBOPTIONS="ctrl:swapcaps"
```

## Swapping command and option on Apple keyboards

Note, the `option` and `command` modifiers on Apple keyboards are different from the standard PC keyboards.
On Apple keyboards, the `option` is to the left of `command` (used as the super/win modifier on Linux).
On PC keyboards it is the other way around.

You can of course switch the `command` and `option` modifiers on your Apple keyboard so it has the standard PC like layout.
There are two ways to do this: By setting the `hid_apple` module parameters (better, requires root), or by using `xmodmap` (worse, no root required).

### Setting the `hid_apple` module parameters

To swap `command` and `option` for your current session, run (as root)

``` shell
echo 1 > /sys/module/hid_apple/parameters/swap_opt_cmd
```

To make the change persistent across reboots, edit or create (as root) `/etc/modprobe.d/hid-apple-local.conf` and include the following: 

    options hid_apple swap_opt_cmd=1

### Using xmodmap

You can alternately swap the `command` and `option` modifiers `xmodmap`.
This, however, isn't ideal as you will have to repeat these steps every time you plug in the keyboard.
You might also have to repeat this every time your computer wakes up from suspend.
However, this method doesn't require root access, so if you don't have root this is your only option.

Save the following snippet to `~/.xmodmaps/swap-command-option.xmodmaprc`:

    remove  mod1        = Alt_L Alt_R Meta_L
    remove  mod4        = Super_L Super_R Hyper_L

    keysym  Alt_L       = Super_L
    keysym  Alt_R       = Super_R
    keysym  Super_L     = Alt_L
    keysym  Super_R     = Alt_R

    add     mod1        = Alt_L Alt_R Meta_L
    add     mod4        = Super_L Super_R Hyper_L

Now run

    xmodmap ~/.xmodmaps/swap-command-option.xmodmaprc

To make the change persistent across sessions, put the above command in your `~/.xinitrc`.
(I recommend also setting a shell alias, since you will have to run it every time you plug in the keyboard.)

## Using function keys without the `FN` modifier (Apple keyboards)

On Apple keyboards, pressing function keys adjusts the brightness / volume, and to get the usual `F1`, `F2` behaviour, you have to use the `FN` modifier.
If you don't want to do this, here is how you can make the function keys on Apple keyboards work, without using the `FN` modifier.

Run (as root)

```shell
echo 2 > /sys/module/hid_apple/parameters/fnmode
```

This will make function keys work without the `FN` modifier for your current session. 
To make the change permanent, then edit or create (as root) `/etc/modprobe.d/hid-apple-local.conf` and include the following:

    options hid_apple fnmode=2

After rebooting, the function keys will work without the `FN` modifier.
