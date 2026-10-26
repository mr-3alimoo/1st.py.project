bill = float(input("ادخل قيمة الفاتورة:"))
eaters = float(input("دخل عدد الاشخاص:"))
share = bill / eaters
tip = float(input("ادخل نسبة البقشيش:"))
total = share + share * tip /100
print(f"كل واحد حسابه: {total:0.2f} جنيه")