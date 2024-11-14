<div align="center"><img src="https://giffiles.alphacoders.com/222/222022.gif"></div>
<h1 align="center">Tsukumo</h1>

**Open Source Package Manager**

Tsukumo is an open-source package manager designed to help developers streamline dependency management across various projects, including custom setups for websites and web applications. With Tsukumo, users can easily set up, install, and manage libraries, plugins, and modules necessary for their websites or other programming projects. It’s built to be versatile and lightweight, making it suitable for a wide range of use cases, from small personal websites to larger, multi-layered applications.

## Key Features

- **Customizable for Any Project**: Tsukumo provides a flexible framework that allows users to set up and configure package management specific to their website or application needs.
- **Dependency Tracking**: Automatically handles dependencies, ensuring that all necessary packages are installed and up to date without conflicts.
- **Cross-Platform Compatibility**: Supports a variety of environments, making it compatible with different operating systems and tech stacks.
- **Open Source & Community-Driven**: Tsukumo is open source, allowing developers to contribute, extend, and tailor the manager for a wide range of use cases.

With its adaptability and simplicity, Tsukumo is designed to be the go-to solution for managing dependencies in any web development environment.

---

## Warning

⚠️ **Early Stages of Development** ⚠️

Please note that Tsukumo is in the **early stages of development** and is **bare-bones** at the moment. It is **not** suitable for production environments or serious use at this time. We recommend using it **only for learning** or **experimental** purposes. Features are still being developed, and the project is not yet stable. Use at your own risk!

---


## Branches

### [Server Branch](https://github.com/999root/Tsukumo/tree/Server)

The **Server** branch contains the backend package manager logic and server-side components for handling package storage, management, and client interactions. This branch is crucial for setting up and maintaining the remote repository for the Tsukumo package manager.

### [Client Branch](https://github.com/999root/Tsukumo/tree/Client)

The **Client** branch contains the client-side package manager, which handles the downloading, installation, and management of packages from the server-side repository. This branch is designed for local package management and is meant for developers who want to use Tsukumo to manage their own packages on their local machines.

---

# Cloning Specific Branches

To set up Tsukumo's **Server** and **Client** components on your local machine, you'll need to clone each branch individually.

## Step 1: Clone the Server Branch

Open your terminal and run the following command to clone the **Server** branch:

```bash
git clone -b Server https://github.com/999root/Tsukumo.git Tsukumo-Server
```

This command will clone only the **Server** branch into a directory named `Tsukumo-Server`. You can change the directory name if desired.

## Step 2: Clone the Client Branch

Similarly, to clone the **Client** branch, run:

```bash
git clone -b Client https://github.com/999root/Tsukumo.git Tsukumo-Client
```

This will create a separate directory named `Tsukumo-Client` with the **Client** branch code.

---

With Tsukumo's separation into **Server** and **Client** branches, you can manage and deploy both the backend and frontend of your package management system independently.
