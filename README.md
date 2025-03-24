# 📶 Wi-Fi Network Monitor

A **real-time network monitoring dashboard** built with Python, Dash, and Plotly.  
This application visualizes **live upload and download speeds** from your network interface on an interactive graph.

---

## 🚀 Features

- Real-time upload and download speed monitoring  
- Updates every 0.5 seconds for smooth visualization  
- Responsive graph using Plotly  
- Clean Bootstrap Dark Theme UI  
- Easy to configure for different network interfaces  

---

## 📂 Project Structure

```
Network-Monitor/
├── app.py              # Main Python application file
└── README.md           # Project documentation
```

---

## 🖥️ Demo Preview

> 
---

## 🔧 Requirements

- Python 3.8 or higher  
- Dash  
- Dash Bootstrap Components  
- psutil  
- numpy  

---



## ⚙️ Configuration

By default, the app monitors the `Wi-Fi` network interface.

#### How to find your network interface name:
```python
import psutil
print(psutil.net_io_counters(pernic=True).keys())
```

#### Update the interface in `app.py` (line 10):
```python
INTERFACE = 'Wi-Fi'
```

#### Common examples:
- Windows: `'Wi-Fi'`  
- Linux: `'wlan0'`  
- MacOS: `'en0'`

---

## ▶️ Running the App

Run the app with:
```bash
python app.py
```

Then open your browser and visit:  
👉 [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## ✨ Screenshots

> 
---

## ✅ To-Do / Future Improvements

- CSV export of speed data  
- Support for multiple network interfaces  
- Bandwidth threshold alerts  
- Docker deployment for remote monitoring  

---

## 🤝 Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a feature branch (`git checkout -b new-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin new-feature`)  
5. Open a Pull Request  

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software with proper attribution.

---

## 🙋‍♂️ Author

Developed by **Thusajiny Ahilakumaran**  
- GitHub: [github.com/yourusername](https://github.com/Athush30)  

---

## 📚 References

- [Dash Documentation](https://dash.plotly.com/)  
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)  
- [psutil Documentation](https://psutil.readthedocs.io/en/latest/)

---



---

### 🎉 Thank You for Checking Out This Project!
