# from decimal import Decimal
# from datetime import datetime
# import random
#
# class Mahsulot:
#     def __init__(self, narx):
#         self._narx = None
#         self.narx = narx
#         self.sana = self.tasodifiy_sana()
#
#     @property
#     def narx(self):
#         return self._narx
#
#     @narx.setter
#     def narx(self, qiymat):
#         # Agar qiymat matn bo‘lsa, uni raqamga aylantirishga urinadi
#         if isinstance(qiymat, str) and qiymat.isdigit():
#             qiymat = Decimal(qiymat)
#
#
#         elif not isinstance(qiymat, Decimal):
#             raise ValueError("Narx faqat musbat raqam ko‘rinishida bo‘lishi kerak.")
#
#
#         if qiymat <= 0:
#             raise ValueError("Narx manfiy yoki 0 bo‘lishi mumkin emas.")
#
#
#         self._narx = qiymat
#
#     @staticmethod
#     def tasodifiy_sana():
#         hozir = datetime.now()
#         tasodifiy_kun = random.randint(0, 10)
#         tasodifiy_soniya = tasodifiy_kun * 86400
#         tasodifiy_vaqt = hozir.timestamp() - tasodifiy_soniya
#         tasodifiy_sana = datetime.fromtimestamp(tasodifiy_vaqt)
#         return tasodifiy_sana.strftime('%d-%m-%Y')
#
#     def yangi_narx(self):
#
#         yangi_narx = self.narx * 12000
#
#         if self.narx < 0:
#             raise ValueError("Chegirma noto‘g‘ri hisoblandi, natija manfiy bo‘lib qoldi.")
#
#         return f"Yangi narx: {yangi_narx} UZS (Sana: {self.sana})"
#
#
# usd = input("Usd ni kiritng : ")
# mahsulot = Mahsulot(usd)
# print(mahsulot.yangi_narx())




# 2 - masala
# import random
# from decimal import Decimal
# from datetime import datetime, timedelta
# class Tovar:
#     def __init__(self, price: Decimal):
#         if price < 0:
#             raise ValueError("manfiy bolishi mumkin emas")
#         self.price = price
#         self.discount_percentage = random.randint(1, 50)
#         self.purchase_date = self.ajratilga_kun()
#         self.foiz = random.randint(2,45)
#     def ajratilga_kun(self):
#         foiz = random.randint(1, 100)
#         randomdan_tanlangan_kun = random.randint(1, 365)
#         return datetime.now() - timedelta(days=randomdan_tanlangan_kun)
#     def __str__(self):
#         return (f"narx: {self.price:.2f} UZS: "
#                 f"chegirma: {self.foiz:.2f} %: "
#                 f"sana: {self.purchase_date.strftime('%d.%m.%Y')}")
#
# try:
#     product = Tovar(Decimal("4664453"))
#     print(product)
# except ValueError as e:
#     print(e)



