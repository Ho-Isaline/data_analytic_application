# 🕷️ Web Crawler Project

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>
  <img src="https://img.shields.io/badge/BeautifulSoup-000000?style=for-the-badge"/>
</div>

## 📖 About
A collection of web crawlers built with Python, featuring implementations for various websites including PTT, Facebook, and Instagram. This project demonstrates different web scraping techniques and data extraction methods.

## 🚀 Features
- 📱 **Multi-Platform Support**
  - PTT Crawler
  - Facebook Crawler
  - Instagram Crawler
- 🔄 **Automated Data Extraction**
- 📊 **Data Processing & Storage**
- 🛡️ **Rate Limiting & Error Handling**

## 🛠️ Tech Stack
- **Python**: Core programming language
- **Selenium**: Web automation and dynamic content scraping
- **BeautifulSoup4**: HTML parsing and data extraction
- **Requests**: HTTP requests handling
- **Pandas**: Data manipulation and storage

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/Ho-Isaline/web_crawl.git
cd web_crawl
```

2. Install required packages
```bash
pip install -r requirements.txt
```

## 📝 Usage

### PTT Crawler
```python
from crawlers.ptt_crawler import PTTCrawler

crawler = PTTCrawler()
crawler.start_crawling('board_name')
```

### Facebook Crawler
```python
from crawlers.fb_crawler import FacebookCrawler

crawler = FacebookCrawler()
crawler.login(username, password)
crawler.crawl_page('page_url')
```

### Instagram Crawler
```python
from crawlers.ig_crawler import InstagramCrawler

crawler = InstagramCrawler()
crawler.crawl_profile('profile_name')
```

## 📋 Prerequisites
- Python 3.7+
- Chrome WebDriver (for Selenium)
- Required Python packages listed in `requirements.txt`

## ⚠️ Important Notes
- Respect websites' robots.txt and terms of service
- Implement appropriate delays between requests
- Handle your credentials securely
- Be mindful of rate limiting and IP blocking

## 🔄 Future Updates
- [ ] Add more platform support
- [ ] Implement proxy rotation
- [ ] Add data visualization features
- [ ] Create comprehensive documentation

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---
<div align="center">
  <i>Built with ❤️ by Isaline Ho</i>
</div>
