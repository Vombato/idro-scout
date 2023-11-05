# Idro Scout

Idro scout is a data scraper usign Selenium Chrome Driver with a built-in Prometheus exporter.

## Installation

Pull the repository, change the values inside the `docker-compose.yml` and run:

```bash
cd scout
docker build -t idro-scout:2.0.0 .
cd ../exposer
docker build -t idro-exposer:2.0.0 .
cd ..
docker-compose up -d
```

## Usage

Connect the exporter to a Prometheus instance.

## Important

This project was made for educational purposes only!

**Always be sure you have permission to scrape websites and respect privacy rules.**

This project is under development so it's not stable at all, if you want to use it, fine. Don't expect any support whatsoever as it's just a proof of concept side project.
