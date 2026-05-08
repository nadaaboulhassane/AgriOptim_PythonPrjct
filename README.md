# 🌾 AgriOptim — Agricultural Optimization

A Python application for optimizing agricultural production under resource constraints using Linear Programming.

## 📋 Features

- **Linear Programming Solver** — Uses scipy.optimize for constraint satisfaction
- **Web Interface** — Flask-based UI with real-time optimization results
- **Multi-crop Planning** — Allocate resources optimally across wheat, corn, and vegetables
- **Resource Management** — Manage constraints: land, water, budget, labor
- **Visual Analytics** — Charts and detailed optimization reports

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

## 📊 Project Structure

- `app.py` — Flask web server
- `models/` — Domain models (Farm, Crop, LinearProgram)
- `solvers/` — Optimization algorithms (Simplex)
- `visualization/` — Charts and reports
- `templates/` — HTML interface

## 👥 Authors

- Nada ABOULHASSANE
- Mohamed Taha AJARROUD

**École Marocaine des Sciences de l'Ingénieur (EMSI)**
