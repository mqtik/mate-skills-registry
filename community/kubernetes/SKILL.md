---
name: kubernetes
description: "Generate and validate Kubernetes manifests (deployments, services, ingress)"
argument-hint: "describe the workload or resource you need to configure"
categories: development, devops, infrastructure
version: 1.0.0
---

Help the user write and validate Kubernetes manifests. When generating Deployments, set resource requests and limits, liveness and readiness probes, and appropriate replica counts. Always use specific image tags, never latest. When writing Services, select the correct type (ClusterIP, NodePort, LoadBalancer) based on the use case. For Ingress resources, include TLS configuration and correct annotations for the ingress controller. When writing ConfigMaps and Secrets, never hardcode sensitive values — reference them from environment variables or external secret managers. Validate manifests for common issues: missing labels, no namespace specified, privileged containers, and missing pod disruption budgets for production workloads. Ask for the Kubernetes version and cloud provider when relevant.
