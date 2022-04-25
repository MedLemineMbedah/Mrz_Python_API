from operator import imod
from unittest import result
from django.shortcuts import render
from django.http import JsonResponse
from numpy import save
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cadorimrest.mrz.mrz.checker.td1 import TD1CodeChecker
from cadorimrest.mrz.mrz.checker.FR.td2 import TD2CodeChecker
from cadorimrest.mrz.mrz.base.countries_ops import is_code
from cadorimrest.mrz.mrz.checker.td3 import TD3CodeChecker


# import easyocr
# import sys
# import re
# from .models import Cart
# from .models import BackCart
# from .models import Book
# from .models import PassePort
# from .serializers import BookSerial
# from .models import Documents


# from django.contrib.auth.forms import UserCreationForm 


# Create Rest pour la lecture de texte dans les image


@api_view(['GET', 'POST'])
def CartMRT(request):

    if request.method == 'GET':
            
            
        mrz_td1 = ("I<MRT00176086916684023233<<<<<\n"
                "9512025M2303174MRT<<<<<<<<<<<7\n"
                "MBEDAH<<MOHAMED<LEMINE<<<<<<<<")
        print(mrz_td1)

        

        # mrz_td1 = ("I<BAD<BAD<<<<<0<<<<<<BAD<<<<<<\n"
        #            "0105998<0512868BAD<<<<BAD<<<<0\n"
        #            "<SPECIMEN1<<SPECIMEN2<<BAD<<<<")

        td1_check = TD1CodeChecker(mrz_td1)

        # td2_check = TD3CodeChecker("I<MRT00176086916684023233<<<<<\n"
        #                            "9512025M2303174MRT<<<<<<<<<<<7\n"
        #                            "MBEDAH<<MOHAMED<LEMINE<<<<<<<<")


        def print_txt(title, value):
            print(title.ljust(20), value)


        fields = td1_check.fields()

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
        imageTexte = {'data': fields}
        
        return JsonResponse(imageTexte)


    elif request.method == 'POST':
        
        data = request.data
        
        a = data['a']
        b = data['b']
        c = data['c']
        mrz_td1 = (a+"\n"+b+"\n"+c)
        
        
        td1_check = TD1CodeChecker(mrz_td1)

        # td2_check = TD3CodeChecker("I<MRT00176086916684023233<<<<<\n"
        #                            "9512025M2303174MRT<<<<<<<<<<<7\n"
        #                            "MBEDAH<<MOHAMED<LEMINE<<<<<<<<")


        def print_txt(title, value):
            print(title.ljust(20), value)


        fields = td1_check.fields()

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
        imageTexte = {'data': fields}
        
        return JsonResponse(imageTexte)


@api_view(['GET', 'POST'])
def CartFr(request):

    if request.method == 'GET':
            

        td2_check = TD2CodeChecker("IDFRAAMADOU<<<<<<<<<<<<<<<<<<<077055\n"
                                    "1807772501026DJIBRIROU<<<<<7512319M3")


        # td2_check = TD2CodeChecker("IDFRAGUISSE<<<<<<<<<<<<<<<<<<<595113\n"
        #                            "1202595062671KUMBA<<<<<<<<<8904104F7")





        def print_txt(title, value):
            print(title.ljust(20), value)


        fields = td2_check.fields()

        print_txt("Type De Document :", fields.document_type)
        print_txt("Pays:", fields.country)
        print_txt("Prenom:", fields.surname)
        print_txt("Nom:", fields.final_hash)
        print_txt("Numero De Document", fields.document_number)
        #print_txt("Doc. Number Hash:", fields.document_number_hash)
        print_txt("Nationalite:", fields.nationality)
        print_txt("Date de naissance:", fields.birth_date)
        #print_txt("Birth Date Hash:", fields.birth_date_hash)
        print_txt("Sex:", fields.sex)
        #print_txt("Expiry Date:",'')
        #print_txt("Expiry Date Hash:", fields.expiry_date_hash)
        print_txt("NNI:", fields.optional_data)
        # print_txt("Final Hash:", '2')
        imageTexte = {'data': fields}
        
        return JsonResponse(imageTexte)


    elif request.method == 'POST':
        
        data = request.data
        
        a = data['a']
        b = data['b']
        mrz_td1 = (a+"\n"+b)

        
      #  td1_check = TD1CodeChecker(mrz_td1)

        # td2_check = TD3CodeChecker("I<MRT00176086916684023233<<<<<\n"
        #                            "9512025M2303174MRT<<<<<<<<<<<7\n"
        #                            "MBEDAH<<MOHAMED<LEMINE<<<<<<<<")

        td2_check = TD2CodeChecker(mrz_td1)


        # td2_check = TD2CodeChecker("IDFRAGUISSE<<<<<<<<<<<<<<<<<<<595113\n"
        #                            "1202595062671KUMBA<<<<<<<<<8904104F7")





        def print_txt(title, value):
            print(title.ljust(20), value)


        fields = td2_check.fields()

        print_txt("Type De Document :", fields.document_type)
        print_txt("Pays:", fields.country)
        print_txt("Prenom:", fields.surname)
        print_txt("Nom:", fields.final_hash)
        print_txt("Numero De Document", fields.document_number)
        #print_txt("Doc. Number Hash:", fields.document_number_hash)
        print_txt("Nationalite:", fields.nationality)
        print_txt("Date de naissance:", fields.birth_date)
        #print_txt("Birth Date Hash:", fields.birth_date_hash)
        print_txt("Sex:", fields.sex)
        #print_txt("Expiry Date:", "")
        #print_txt("Expiry Date Hash:", fields.expiry_date_hash)
        print_txt("NNI:", fields.optional_data)
        # print_txt("Final Hash:", '2')
        imageTexte = {'data': fields}
        
        return JsonResponse(imageTexte)




@api_view(['GET', 'POST'])
def PassPort(request):

    if request.method == 'GET':
            
                
        # mrz_td3 = ("P<FRASOUMARE<<AMINATA<<<<<<<<<<<<<<<<<<<<<<<\n"
        #         "15CE559544FRA8809173F2506023<<<<<<<<<<<<<<02")

        mrz_td3 =("P<MRTMBIDAH<<MOHAMED<LEMINE<<<<<<<<<<<<<<<<<\n"
                "BG49926612MRT9512025M2207124<<<<<<<<<<<<<<<0")

        td3_check = TD3CodeChecker(mrz_td3, check_expiry=True)

        print(td3_check.mrz_code)

        if not td3_check:
            print("Falses:", td3_check.report.falses)
            print("Warnings:", td3_check.report.warnings)

        print("'%s' is code: %s" % (td3_check._country, str(is_code("ASU"))))


        def print_txt(title, value):
            print(title.ljust(20), value)


        fields = td3_check.fields()


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

        imageTexte = {'data': fields}
        
        return JsonResponse(imageTexte)


    elif request.method == 'POST':
        
        data = request.data
        
        a = data['a']
        b = data['b']
        mrz_td1 = (a+"\n"+b)

        # mrz_td3 =("P<MRTMBIDAH<<MOHAMED<LEMINE<<<<<<<<<<<<<<<<<\n"
        #         "BG49926612MRT9512025M2207124<<<<<<<<<<<<<<<0")

        td3_check = TD3CodeChecker(mrz_td1, check_expiry=True)

        print(td3_check.mrz_code)

        if not td3_check:
            print("Falses:", td3_check.report.falses)
            print("Warnings:", td3_check.report.warnings)

        print("'%s' is code: %s" % (td3_check._country, str(is_code("ASU"))))


        def print_txt(title, value):
            print(title.ljust(20), value)


        fields = td3_check.fields()


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

        imageTexte = {'data': fields}
        
        return JsonResponse(imageTexte)

        
