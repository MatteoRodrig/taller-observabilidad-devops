# Taller de Observabilidad y Monitoreo - DevOps

Este repositorio contiene la solución integral para el taller de Observabilidad y Monitoreo del curso de Introducción a DevOps (Universidad Nacional de Colombia - Sede Manizales).

## 👥 Integrantes del Equipo
* **Julian Mateo Rodríguez Díaz**
* **Daniela Fernanda Mendoza Epia**

## 📋 Descripción del Proyecto
El objetivo de este proyecto es desplegar una arquitectura de observabilidad completa para una aplicación web desarrollada en Python (Flask). El entorno incluye:
* **Aplicación Flask:** Expone un endpoint `/metrics` para la recolección de datos.
* **Prometheus:** Motor encargado de hacer *scraping* cada 5 segundos a la aplicación.
* **Grafana:** Plataforma para la visualización de las métricas en tiempo real.
* **Docker & Docker Compose:** Para garantizar entornos reproducibles y aislados.
* **GitHub Actions:** Implementación de Pipelines CI/CD para la construcción, despliegue y monitoreo automatizado en AWS EC2.

## 📁 Estructura del Repositorio
* `app/`: Código fuente de la aplicación Flask y su respectivo Dockerfile.
* `monitoring/`: Archivos de configuración de Prometheus (`prometheus.yml`).
* `docker-compose.yml`: Orquestación de los servicios (App, Prometheus y Grafana).
* `.github/workflows/`: Definición de los 3 pipelines CI/CD (`build.yml`, `deploy-app.yml`, `deploy-monitoring.yml`).

## 🚀 Despliegue Local
Para levantar este entorno en cualquier máquina con Docker instalado, ejecutar:
```bash
docker compose up -d
