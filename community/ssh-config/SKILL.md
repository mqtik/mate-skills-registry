---
name: ssh-config
description: "Generate and manage SSH config files, keys, and tunnels"
argument-hint: "describe the server, tunnel, or SSH task you need help with"
categories: development, devops, security
version: 1.0.0
---

Help the user configure SSH. When generating ~/.ssh/config entries, set Host alias, HostName, User, Port, IdentityFile, and useful options like ServerAliveInterval, ServerAliveCountMax, and ControlMaster for connection reuse. When setting up tunnels, generate the correct -L (local), -R (remote), or -D (dynamic/SOCKS) flags and explain the port forwarding direction. When generating key pairs, recommend ed25519 over RSA, suggest a strong passphrase, and provide the commands to generate and copy the public key to the server. When diagnosing connection issues, ask for the verbose output (-vvv) and identify the failing handshake step. Never generate or store private key material — only help with commands and config structure.
