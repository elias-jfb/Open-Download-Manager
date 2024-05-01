
<p align="center">
  <a href="https://github.com/liwei-gif/Open-Download-Manager/releases"><img src="https://img.shields.io/github/release/liwei-gif/Open-Download-Manager" alt="Release version"></a>
  <a href="https://github.com/liwei-gif/Open-Download-Manager/actions/workflows/release.yml"><img src="https://github.com/liwei-gif/Open-Download-Manager/workflows/Build/badge.svg" alt="Build status"></a>
  <a href="https://github.com/liwei-gif/Open-Download-Manager/actions/workflows/beta-pack.yml"><img src="https://github.com/liwei-gif/Open-Download-Manager/workflows/Build%20Beta/badge.svg" alt="Build status"></a>
  <a href="https://github.com/liwei-gif/Open-Download-Manager/tree/dev"><img src="https://img.shields.io/github/package-json/v/liwei-gif/Open-Download-Manager/dev" alt="Dev branch version"></a>
</p>

<h2 align="center">Open Download Manager</h2>

### Description

Welcome to Open Download Manager v1.0, an open-source, multi-threaded file downloader developed using Python and Tkinter. This tool is designed to help you download files from the internet in multiple parts concurrently, potentially increasing the download speed by leveraging multiple server connections.

### Features

- **User-Friendly Interface**: Built with Tkinter, the interface is simple yet functional, allowing you to input download links directly.
- **Multi-threaded Downloads**: Downloads files in multiple parts simultaneously, which can speed up the overall download time.
- **Customizable Segments**: You can specify the number of parts in which you want to download a file, giving you control over the download process.

### How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/liwei-gif/Open-Download-Manager.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Open-Download-Manager
   ```
3. **Run the Application**:
   ```bash
   python download_manager.py
   ```

Once the application is running:
- Enter the URL of the file you wish to download in the URL field.
- Specify the number of parts you want the file to be split into for downloading.
- Click the 'Download' button to start the download process.

### Requirements

- Python 3.x
- `tkinter` module for the GUI
- `requests` module for handling HTTP requests
- `threading` for managing multiple download threads

### Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

### Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/liwei-gif/Open-Download-Manager](https://github.com/liwei-gif/Open-Download-Manager)

---

We hope you find Open Download Manager useful for your downloading needs. Feel free to fork the repo and contribute to making it better!
