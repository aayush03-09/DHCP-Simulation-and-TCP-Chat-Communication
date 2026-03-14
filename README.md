# DHCP Simulation and LAN Chat System

## Project Overview
This project demonstrates a **DHCP (Dynamic Host Configuration Protocol) simulation** along with a **LAN-based chat system** implemented using Python socket programming. The project shows how devices automatically obtain IP addresses from a DHCP server and how two devices can communicate over a local network.

The implementation was tested using **two laptops connected to the same LAN network**.

---

# Features

### DHCP Simulation
- Automatic IP address allocation
- DHCP DORA process implementation
- IP pool management
- 30-second lease time
- IP release and reuse
- Server-client communication using **UDP sockets**

### LAN Chat System
- Real-time messaging between two laptops
- Client-server architecture
- Reliable communication using **TCP sockets**
- Message sending and receiving in a loop

---

# Technologies Used

- Python 3
- Socket Programming
- UDP Protocol (DHCP simulation)
- TCP Protocol (Chat system)
- JSON for message formatting

---

# Project Structure

---

# How DHCP Works in This Project

The DHCP simulation follows the **DORA process**:

1. **Discover**  
   Client broadcasts a message requesting an IP address.

2. **Offer**  
   DHCP server offers an available IP from its pool.

3. **Request**  
   Client requests the offered IP address.

4. **Acknowledge**  
   Server confirms and assigns the IP address with a lease time.

The server manages an **IP pool** and tracks assigned addresses.

---

# Lease Time

The project implements a **30-second lease time**.

After the lease expires:
- The assigned IP is released
- The IP returns to the available pool
- Another client can use it

---

# Chat System Workflow

The chat system works using **TCP sockets**.

1. Chat server starts and listens on port **6000**
2. Chat client connects using server IP
3. Client sends message
4. Server receives message
5. Server sends reply
6. Communication continues in a loop

---

# How to Run the Project

## Step 1: Start DHCP Server
Run on the server laptop:

---

## Step 2: Run DHCP Client
Run on the client laptop:

---

## Step 3: Start Chat Server
Run on server laptop:

---

## Step 3: Start Chat Server
Run on server laptop:

---

## Step 4: Start Chat Client
Run on client laptop:

---

# Learning Outcomes

This project helped in understanding:

- DHCP protocol working
- Dynamic IP allocation
- Lease time management
- Socket programming
- UDP vs TCP communication
- Client-server architecture
- LAN networking between multiple devices

---

# Future Improvements

- Multi-client DHCP support
- GUI-based chat application
- File transfer system
- DHCP logging system
- Advanced lease management

---

# Author

Your Name  
Networking Project – DHCP Simulation and LAN Chat System
