from django.contrib import admin
from .models import TableModelPays, moneyresources, budgetitems,projects, Departments, countryes, RegPay, currencyes, Banks, regions, parentcountrypartyes, deals, typeofdeals, groupdeals, ModelPays, countrypartyes, typeofoperations, typeofpays, organizations, bankcards

admin.site.register([Departments,
                     countryes,
                     RegPay,
                     currencyes,
                     Banks,
                     regions,
                     parentcountrypartyes,
                     deals,
                     typeofdeals,
                     groupdeals,
                     ModelPays,
                     countrypartyes,
                     typeofoperations,
                     typeofpays,
                     organizations,
                     bankcards,
                     TableModelPays,
                     moneyresources,
                     budgetitems,
                     projects])

