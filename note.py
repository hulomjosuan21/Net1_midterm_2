Router 1:
    int f0/0
    ip add 50.0.1.1 255.255.255.128
    no shut
    exit
    int s1/0
    ip add 50.0.0.33 255.255.255.224
    no shut

Router 2:
    int f0/0
    ip add 50.0.1.129 255.255.255.128
    no shut
    exit
    int s1/0
    ip add 50.0.0.34 255.255.255.224
    no shut    
    int s1/1
    ip add 50.0.0.65 255.255.255.240
    no shut    

Router 3:
    int f0/0
    ip add 50.0.6.1 255.255.255.0
    no shut
    exit
    int s1/0
    ip add 50.0.0.66 255.255.255.240
    no shut
    int s1/1
    ip add 50.0.0.193 255.255.255.224
    no shut

Router 4:
    int f0/0
    ip add 50.0.8.1 255.255.255.0
    no shut
    int s1/0
    ip add  50.0.0.194 255.255.255.224
    no shut

Pc 1:
    int f0/0
    ip add 50.0.1.2 255.255.255.128
    no shut
    no ip routing

Pc 2:
    int f0/0
    ip add 50.0.1.130 255.255.255.128
    no shut
    no ip routing

Pc 3:
    int f0/0
    ip add 50.0.7.1 255.255.255.0
    no shut
    no ip routing

Pc 4:
    int f0/0
    ip add 50.0.9.1 255.255.255.0
    no shut
    no ip routing


use ip route to the routers so that all the Pcs can ping to other Pcs

Sure, you can use the `ip route` command to manually set up routing on each router. Here's how you can do it:

```bash
Router 1:
    ip route 50.0.1.128 255.255.255.128 50.0.0.34
    ip route 50.0.6.0 255.255.255.0 50.0.0.34
    ip route 50.0.8.0 255.255.255.0 50.0.0.34
    ip route 50.0.7.0 255.255.255.0 50.0.0.34
    ip route 50.0.9.0 255.255.255.0 50.0.0.34

Router 2:
    ip route 50.0.1.0 255.255.255.128 50.0.0.33
    ip route 50.0.6.0 255.255.255.0 50.0.0.66
    ip route 50.0.8.0 255.255.255.0 50.0.0.194
    ip route 50.0.7.0 255.255.255.0 50.0.0.66
    ip route 50.0.9.0 255.255.255.0 50.0.0.194

Router 3:
    ip route 50.0.1.0 255.255.255.128 50.0.0.34
    ip route 50.0.1.128 255.255.255.128 50.0.0.34
    ip route 50.0.8.0 255.255.255.0 50.0.0.194
    ip route 50.0.7.0 255.255.255.0 50.0.0.34
    ip route 50.0.9.0 255.255.255.0 50.0.0.194

Router 4:
    ip route 50.0.1.0 255.255.255.128 50.0.0.34
    ip route 50.0.1.128 255.255.255.128 50.0.0.34
    ip route 50.0.6.0 255.255.255.0 50.0.0.66
    ip route 50.0.7.0 255.255.255.0 50.0.0.66
    ip route 50.0.9.0 255.255.255.0 50.0.0.66
```

This will ensure that all the PCs can ping each other. Please replace the IP addresses and subnet masks with your actual network configuration if it's different. Also, remember to save your configuration changes on each router.