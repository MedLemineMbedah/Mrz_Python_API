#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mrz.checker.td3 import TD3CodeChecker

from mrz.checker.td1 import TD1CodeChecker

mrz_td1 = ("I<MRT00176086916684023233<<<<<\n"
           "9512025M2303174MRT<<<<<<<<<<<7\n"
           "MBEDAH<<MOHAMED<LEMINE<<<<<<<<")


# mrz_td1 = ("I<BAD<BAD<<<<<0<<<<<<BAD<<<<<<\n"
#            "0105998<0512868BAD<<<<BAD<<<<0\n"
#            "<SPECIMEN1<<SPECIMEN2<<BAD<<<<")

td2_check = TD1CodeChecker(mrz_td1)

# td2_check = TD3CodeChecker("I<MRT00176086916684023233<<<<<\n"
#                            "9512025M2303174MRT<<<<<<<<<<<7\n"
#                            "MBEDAH<<MOHAMED<LEMINE<<<<<<<<")


def print_txt(title, value):
    print(title.ljust(20), value)


fields = td2_check.fields()

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
