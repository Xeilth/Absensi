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
    if kodeDosen == "TI126L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[83]").click()
    if kodeDosen == "TI117L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[98]").click()
    if kodeDosen == "NN257L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[2]/td[2]/select/option[96]").click()
    if kodeDosen == "NN056L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[2]/td[2]/select/option[18]").click()
    if kodeDosen == "TI041L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[2]/td[2]/select/option[127]").click()
    if kodeDosen == "TI125L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[2]/td[2]/select/option[118]").click()
    if kodeDosen == "NN258L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[2]/td[2]/select/option[97]").click()
    if kodeDosen == "NN222L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[2]/td[2]/select/option[84]").click()
    if kodeDosen == "TI122L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[2]/td[2]/select/option[75]").click()
    if kodeDosen == "NN208L":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[2]/td[2]/select/option[74]").click()

kodeMatkul = "TI43274"
kelas = "B"
def Matkul():
    if kodeMatkul == "TI43274" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[4]").click()
    if kodeMatkul == "TI43274" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[3]").click()
    if kodeMatkul == "TI43274" and kelas == "C":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[5]").click()
    if kodeMatkul == "TI43142" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[2]").click()
    if kodeMatkul == "TI43142" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[3]").click()
    if kodeMatkul == "TI43284" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[4]").click()
    if kodeMatkul == "TI43284" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[5]").click()
    if kodeMatkul == "TI43284" and kelas == "C":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p/table/tbody/tr[3]/td[2]/select/option[6]").click()
    if kodeMatkul == "TI43446" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[2]").click()
    if kodeMatkul == "TI3466" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[3]").click()
    if kodeMatkul == "TI3466" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[4]").click()
    if kodeMatkul == "TI3466" and kelas == "C":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[5]").click()
    if kodeMatkul == "TI41092" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[2]").click()
    if kodeMatkul == "TI41092" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[3]").click()
    if kodeMatkul == "TI43436" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[4]").click()
    if kodeMatkul == "TI43456" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[5]").click()
    if kodeMatkul == "TI43456" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[8]").click()
    if kodeMatkul == "TI43456" and kelas == "C":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[7]").click()
    if kodeMatkul == "LB42052" and kelas == "E":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[8]").click()
    if kodeMatkul == "LB42052" and kelas == "F":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[9]").click()
    if kodeMatkul == "TI41112" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[2]").click()
    if kodeMatkul == "TI41112" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[3]").click()
    if kodeMatkul == "TI41254" and kelas == "A":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[4]").click()
    if kodeMatkul == "TI41254" and kelas == "B":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[5]").click()
    if kodeMatkul == "TI41254" and kelas == "C":
        driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[1]/table/tbody/tr[3]/td[2]/select/option[6]").click()

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
        data = driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[4]/table/tbody/tr["+str(index)+"]/td[2]").text
        index += 1
        print(i)
        print(data)

        for j in mahasiswa:
            if data == j:
                print("Hadir")

def Refresh():
    driver.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[3]/tbody/tr[1]/td[2]/p[2]/table/tbody/tr[5]/td/input[3]").click()
