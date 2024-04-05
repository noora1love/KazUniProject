from django.db import models
from django.forms import IntegerField


class typeofoperations(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
            return f'{self.name}'
class typeofpays(models.Model):
        name = models.CharField(max_length=50, null=False, blank=False)
        def __str__(self):
                return f'{self.name}'
class organizations(models.Model):
        id1c = models.CharField(max_length=50, null=True, blank=True)
        code = models.CharField(max_length=50, null=True, blank=True)
        name = models.CharField(max_length=50, null=False, blank=False)
        bin = models.IntegerField(null=True, blank=True)

        def __str__(self):
                return f'{self.name}'
class budgetitems(models.Model):
        ISAGROUP_CHOISES = {
                "G" : "Group",
                "N" : "No_Group"
        }
        id1c = models.CharField(max_length=50, null=True, blank=True)
        code = models.CharField(max_length=9, null=True, blank=True)
        name = models.CharField(max_length=50, null=False, blank=False)
        isgroup = models.BooleanField(default=False)
        def __str__(self):
                return f'{self.name}'
class projects(models.Model):
        id1c = models.CharField(max_length=50, null=True, blank=True)
        code = models.CharField(max_length=50, null=True, blank=True)
        name = models.CharField(max_length=50)
        isgroup = models.BooleanField(default=False)
        parent = models.ForeignKey(budgetitems,on_delete=models.CASCADE)
        def __str__(self):
                return f'{self.name}'
class countryes(models.Model):
        name = models.CharField(max_length=50)
        def __str__(self):
                return f'{self.name}'
class parentcountrypartyes (models.Model):
        name = models.CharField(max_length=50)
        def __str__(self):
                return f'{self.name}'
class regions (models.Model):
        name = models.CharField(max_length=50)
        def __str__(self):
                return f'{self.name}'
class groupdeals(models.Model):
        name = models.CharField(max_length=50, null=False, blank=False)
        def __str__(self):
                return f'{self.name}'
class typeofdeals(models.Model):
        name = models.CharField(max_length=50, null=False, blank=False)
        def __str__(self):
                return f'{self.name}'
class countrypartyes(models.Model):

        id1c = models.CharField(max_length=50, null=True, blank=True)
        code = models.CharField(max_length=50, null=True, blank=True)
        name = models.CharField(max_length=50, null=False, blank=False)
        fullname = models.CharField(max_length=50, null=True, blank=True)
        bin = models.CharField(max_length=30, null=True, blank=True)
        kbe = models.CharField(max_length=2, null=True, blank=True)
        def __str__(self):
                return f'{self.name}'
class deals(models.Model):
        id1c = models.CharField(max_length=50, null=True, blank=True)
        code = models.CharField(max_length=50, null=True, blank=True)
        name = models.CharField(max_length=50, null=False, blank=False)
        owner = models.ForeignKey(countrypartyes, on_delete=models.CASCADE)
        organization = models.ForeignKey(organizations, on_delete=models.CASCADE, null=True, blank=True)
        def __str__(self):
                return f'{self.name}'
class bankcards(models.Model):
        name = models.CharField(max_length=50, null=False, blank=False)
        def __str__(self):
                return f'{self.name}'
class currencyes(models.Model):
        name = models.CharField(max_length=50)
        fullname = models.CharField(max_length=50)
        def __str__(self):
                return f'{self.name}'
class Banks(models.Model):
        name = models.CharField(max_length=50)
        def __str__(self):
                return f'{self.name}'
class moneyresources(models.Model):
        id1c = models.CharField(max_length=50, null=False, blank=False)
        code = models.CharField(max_length=50, null=True, blank=True)
        name = models.CharField(max_length=50, null=False, blank=False)
        typeofpay = models.ForeignKey(typeofpays, on_delete=models.CASCADE)
        currency = models.ForeignKey(currencyes, on_delete=models.CASCADE, null=True, blank=True)
        numberofcheck = models.CharField(max_length=50, null=True, blank=True)
        bank = models.ForeignKey(Banks, on_delete=models.CASCADE, null=True)
        def __str__(self):
                return f'{self.name}'
class ModelPays(models.Model):
        id1c = models.CharField(max_length=50, null=True, blank=True)
        title = models.CharField(max_length=200, null=True, blank=True)
        numberofdocument = models.IntegerField(null=True, blank=True)
        dateofstart = models.DateField(null=True, blank=True)
        dateofend = models.DateField(default=2005)
        typeofpay = models.ForeignKey(typeofpays, on_delete=models.CASCADE)
        organization = models.ForeignKey(organizations, on_delete=models.CASCADE)
        moneyresource = models.ForeignKey(moneyresources, on_delete=models.CASCADE, null=True, blank=True)
        typeofoperation = models.ForeignKey(typeofoperations, on_delete=models.CASCADE)
        currency = models.ForeignKey(currencyes, on_delete=models.CASCADE, null=True, blank=True)
        countrparty = models.ForeignKey(countrypartyes, on_delete=models.CASCADE)
        bankcard = models.ForeignKey(bankcards, on_delete=models.CASCADE)
        comments = models.CharField(max_length=25000, null=True, blank=True)

        def __str__(self):
                return f'Название : {self.title}'

class TableModelPays(models.Model):
        numberofline = models.IntegerField(null=True, blank=True)
        dealofcountrparty = models.ForeignKey(deals, on_delete=models.CASCADE)
        paymentamount = models.IntegerField(null=True, blank=True)
        budgetitem = models.ForeignKey(budgetitems, on_delete=models.CASCADE)
        project = models.ForeignKey(projects, on_delete=models.CASCADE)

class Departments(models.Model):
        name = models.CharField(max_length=50)
        def __str__(self):
                return f'{self.name}'


class RegPay(models.Model):
        name = models.CharField(max_length=50, null=False, blank=False)
        model_pays = models.ManyToManyField(ModelPays)
        contractNumber = models.CharField(max_length=50)
        Department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=False)
        paymentDestination = models.CharField(max_length=250)
        currency = models.ForeignKey(currencyes, on_delete=models.CASCADE)
        budgetItem = models.CharField(max_length=250)
        amounOfPayment = models.CharField(max_length=250)
        nameOfBank = models.ForeignKey(Banks, on_delete=models.CASCADE)
        def __str__ (self):
                return f'{self.name}'


