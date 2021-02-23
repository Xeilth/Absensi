from selenium import webdriver
from time import sleep

import config


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://siap.poltekpos.ac.id/siap/besan.depan.php")

def LoginSiap():
    user = config.username
    passw = config.password

    username = driver.find_elements_by_class_name("textbox")[0]
    username.send_keys(user)

    sleep(1)

    password = driver.find_elements_by_class_name("textbox")[1]
    password.send_keys(passw)

    sleep(1)

    login = driver.find_element_by_class_name("button")
    login.click()

def run():
    LoginSiap()
    ClickAbsen()
    TahunAkad()
    Dosen()
    Matkul()
    TambahPresensi()
    simpan()
    AddMahasiswa()
    Mahasiswa()
    Refresh()

def ClickAbsen():
    driver.find_elements_by_class_name("side")[-1].click()

def TahunAkad():
    driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[1]/td[3]/select/option[2]").click()

kodeDosen = "TI126L"
def Dosen():
    base_option_xpath = "/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/"
    list_kodeDosen = {
    "TI126L": "p/table/tbody/tr[2]/td[2]/select/option[83]", 
    "TI117L":"p/table/tbody/tr[2]/td[2]/select/option[98]", 
    "NN257L":"p/table/tbody/tr[2]/td[2]/select/option[96]", 
    "NN056L":"p[1]/table/tbody/tr[2]/td[2]/select/option[18]", 
    "TI041L":"p[1]/table/tbody/tr[2]/td[2]/select/option[127]", 
    "TI125L":"p[1]/table/tbody/tr[2]/td[2]/select/option[118]", 
    "NN258L":"p[1]/table/tbody/tr[2]/td[2]/select/option[97]", 
    "NN222L":"p[1]/table/tbody/tr[2]/td[2]/select/option[84]", 
    "TI122L":"p[1]/table/tbody/tr[2]/td[2]/select/option[75]", 
    "NN208L":"p[1]/table/tbody/tr[2]/td[2]/select/option[74]"}
    
    for kode, xpath in list_kodeDosen.items():
        if kodeDosen == kode:
            driver.find_element_by_xpath(f"{base_option_xpath}{xpath}").click()

kodeMatkul = "TI43274"
kelas = "B"
def Matkul():
    base_option_xpath = "/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/"
    list_kodeMatkul = [
    ("TI43274", "A", "p/table/tbody/tr[3]/td[2]/select/option[3]"),
    ("TI43274", "B", "p/table/tbody/tr[3]/td[2]/select/option[4]"),
    ("TI43274", "C", "p/table/tbody/tr[3]/td[2]/select/option[5]"),

    ("TI43142", "A", "p/table/tbody/tr[3]/td[2]/select/option[2]"),
    ("TI43142", "B", "p/table/tbody/tr[3]/td[2]/select/option[3]"),

    ("TI43284", "A", "p/table/tbody/tr[3]/td[2]/select/option[4]"),
    ("TI43284", "B", "p/table/tbody/tr[3]/td[2]/select/option[5]"),
    ("TI43284", "C", "p/table/tbody/tr[3]/td[2]/select/option[6]"),

    ("TI43446", "A", "p[1]/table/tbody/tr[3]/td[2]/select/option[2]"),

    ("TI3466", "A", "p[1]/table/tbody/tr[3]/td[2]/select/option[3]"),
    ("TI3466", "B", "p[1]/table/tbody/tr[3]/td[2]/select/option[4]"),
    ("TI3466", "C", "p[1]/table/tbody/tr[3]/td[2]/select/option[5]"),

    ("TI41092", "A", "p[1]/table/tbody/tr[3]/td[2]/select/option[2]"),
    ("TI41092", "B", "p[1]/table/tbody/tr[3]/td[2]/select/option[3]"),

    ("TI43436", "A", "p[1]/table/tbody/tr[3]/td[2]/select/option[4]"),

    ("TI43456", "A", "p[1]/table/tbody/tr[3]/td[2]/select/option[5]"),
    ("TI43456", "B", "p[1]/table/tbody/tr[3]/td[2]/select/option[8]"),
    ("TI43456", "C", "p[1]/table/tbody/tr[3]/td[2]/select/option[7]"),

    ("LB42052", "E", "p[1]/table/tbody/tr[3]/td[2]/select/option[8]"),
    ("LB42052", "F", "p[1]/table/tbody/tr[3]/td[2]/select/option[9]"),

    ("TI41112", "A", "p[1]/table/tbody/tr[3]/td[2]/select/option[2]"),
    ("TI41112", "B", "p[1]/table/tbody/tr[3]/td[2]/select/option[3]"),

    ("TI41254", "A", "p[1]/table/tbody/tr[3]/td[2]/select/option[4]"),
    ("TI41254", "B", "p[1]/table/tbody/tr[3]/td[2]/select/option[5]"),
    ("TI41254", "C", "p[1]/table/tbody/tr[3]/td[2]/select/option[6]"),]

    for item in list_kodeMatkul:
        if kodeMatkul == item[0] and kelas == item[1]:
            driver.find_element_by_xpath(f"{base_option_xpath}{item[2]}").click()

def TambahPresensi():
    driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[2]/table/tbody/tr[5]/td/input[2]").click()

def simpan():
    driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[3]/table/tbody/tr[7]/td/input[1]").click()

def AddMahasiswa():
    driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[3]/table/tbody/tr[4]/td[8]/a").click()

def Mahasiswa():
    mahasiswa = ["1184004", "1184007", "1184011", "1184010", "1184047"]

    jumMahasiswa = int(driver.find_elements_by_class_name("inp1")[-1].text)
    print(jumMahasiswa)

    index = 1
    for i in range(jumMahasiswa):
        data = driver.find_element_by_xpath(f"/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[4]/table/tbody/tr[{index}]/td[2]").text
        index += 1
        print(i)
        print(data)

        for j in mahasiswa:
            if data == j:
                print("Hadir")

def Refresh():
    driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[2]/table/tbody/tr[5]/td/input[3]").click()
