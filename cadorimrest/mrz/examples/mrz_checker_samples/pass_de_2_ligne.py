#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.base.countries_ops import is_code
from mrz.checker.td3 import TD3CodeChecker

# mrz_td3 =("IDFRAAMADOU<<<<<<<<<<<<<<<<<<<077055\n"
#           "1807772501026DJIBRIROU<<<<<7512319M3")

# mrz_td3 =("P<MRTMBIDAH<<MOHAMED<LEMINE<<<<<<<<<<<<<<<<<\n"
#             "BG49926612MRT9512025M2207124<<<<<<<<<<<<<<<0")


mrz_td3 = ("P<FRASOUMARE<<AMINATA<<<<<<<<<<<<<<<<<<<<<<<\n"
           "15CE559544FRA8809173F2506023<<<<<<<<<<<<<<02")

td3_check = TD3CodeChecker(mrz_td3, check_expiry=True)

print(td3_check.mrz_code)

if not td3_check:
    print("Falses:", td3_check.report.falses)
    print("Warnings:", td3_check.report.warnings)

print("'%s' is code: %s" % (td3_check._country, str(is_code("ASU"))))


def print_txt(title, value):
    print(title.ljust(20), value)


fields = td3_check.fields()

# print_txt("Document Type:", fields.document_type)
# print_txt("Country:", fields.country)
# print_txt("Surname:", fields.surname)
# print_txt("Name:", fields.name)
# print_txt("Doc. Number", fields.document_number)
# print_txt("Doc. Number Hash:", fields.document_number_hash)
# print_txt("Nationality:", fields.nationality)
# print_txt("Birth Date:", fields.birth_date)
# print_txt("Birth Date Hash:", fields.birth_date_hash)
# print_txt("Sex:", fields.sex)
# print_txt("Expiry Date:", fields.expiry_date)
# print_txt("Expiry Date Hash:", fields.expiry_date_hash)
# print_txt("Optional data:", fields.optional_data)
# print_txt("Optional data hash:", fields.optional_data_hash)
# print_txt("Final Hash:", fields.final_hash)


print_txt("Type De Document : ", fields.document_type)
print_txt("Pays:", fields.country)
print_txt("Nom De Famille:", fields.surname)
print_txt("Nom :", fields.name)
print_txt("Numero De Document", fields.document_number)
print_txt("Doc. Number Hash:", fields.document_number_hash)
print_txt("Nationalite:", fields.nationality)
print_txt("Date de naissance:", fields.birth_date)
print_txt("Hachage de la date de naissance:", fields.birth_date_hash)
print_txt("Sex:", fields.sex)
print_txt("Date d'expiration:", fields.expiry_date)
print_txt("Hachage de la date d'expiration :", fields.expiry_date_hash)
print_txt("NNI:", fields.optional_data)
print_txt("Hachage final:", fields.final_hash)
