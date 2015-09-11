name: GI
avatar: http://cdn.libravatar.org/avatar/1d9eff8253e59f5c7c243a8c558e4f98c0b2d3df3533dc05a5da7adffc798be2
subject: Traffic to guest extremely slow after upgrade to 1.1.2+dfsg-6+deb7u3
date: 2014-06-18 17:31:13

After upgrading I found that the network on my host machine was dropping up to 20% of incoming packets.
This had the effect of reducing the incoming speed to less than 100kbps, while the outgoing speed was a good 20mbps+.

I found that setting the device model to `virtio` fixed it. (The device model was `Default` earlier.)
