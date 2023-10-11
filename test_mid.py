import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
def test_laboratorium_site_interaction(browser):
    browser.get("https://pyapp.unhas.ac.id/laboratorium/")      

    bar_elements = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'apexcharts-bar-area')]"))
    )
    
    # bar_elements = browser.find_elements(By.XPATH, "//*[contains(@class, 'apexcharts-bar-area')]")
    bar_elements[0].click()
    time.sleep(5)    
    
    # Temukan semua tautan menggunakan selector
    links_elements = browser.find_elements(By.CSS_SELECTOR, "#fak_content ul li a")
    print(f"Found {len(links_elements)} link elements")
    # Pastikan ada setidaknya satu tautan sebelum melanjutkan
    
    print("There are links. Processing the first link.")
    # Mengambil tautan pertama
    link = links_elements[0]

    # Pastikan tautan dapat diklik
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#fak_content ul li a"))
    )
    
    process_link(link, browser)

    num_of_links = len(browser.find_elements(By.CSS_SELECTOR, "#main_content ul.list-group > li.list-group-item a"))

    # Loop berdasarkan jumlah tautan
    for i in range(1, num_of_links):
        link2 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"#main_content ul.list-group > li.list-group-item:nth-child({i+1}) a"))
        )
        process_link(link2, browser)    

def process_link(link_element, browser):
    
    link_element.location_once_scrolled_into_view
    time.sleep(2)
    link_element.click()
    time.sleep(2)
    
    # Dapatkan elemen yang berisi teks 'Jumlah'
    jumlah_elements = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.col-md-2.text-nowrap"))
    )

    # Inisialisasi variabel untuk menyimpan total peralatan
    total_peralatan = 0

    # Loop melalui semua elemen dan ekstrak jumlah
    for element in jumlah_elements:
        print(f"Element text: {element.text}")
        text = element.text
        if 'Jumlah' in text:
            # Ekstrak angka dari teks dan tambahkan ke total
            num = int(text.split('Jumlah')[1].strip())
            total_peralatan += num

    print("Total Peralatan:", total_peralatan)

    # Klik tombol "Kembali" untuk kembali ke halaman sebelumnya
    back_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.ml-auto.btn.btn-link'))
    )
    
    back_button.location_once_scrolled_into_view
    time.sleep(5)

    back_button.click()

    # Tunggu sejenak lagi agar halaman asli dapat dimuat kembali dengan benar
    time.sleep(5)

    return total_peralatan
