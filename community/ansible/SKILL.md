---
name: ansible
description: "Write Ansible playbooks, roles, and inventory files"
argument-hint: "describe the automation task or server configuration you need"
categories: development, devops, infrastructure
version: 1.0.0
---

Help the user write Ansible automation. When writing playbooks, use descriptive task names, set become: true only where needed, and handle errors with block/rescue. When creating roles, follow the standard directory structure (tasks, handlers, templates, vars, defaults, meta) and keep roles single-purpose. When writing inventory files, group hosts logically and use host_vars and group_vars for configuration. Use Jinja2 templates for config files that vary per host. When installing packages, use the package module for OS-agnostic playbooks when possible. Flag non-idempotent tasks that use shell or command when a dedicated module exists. Always include a handlers section to restart services only when configuration changes. Ask for the target OS distribution before generating package installation tasks.
