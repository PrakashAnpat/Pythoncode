print("Using flag")
print("% d"%123)
print("%+d"%(123))
print("% d %d"%(123,789))
print("% s"%"Prakash")
print("% f"%123.678)
print("% f% f"%(123.678,123.765))
print("Using width")
print("%8d"%123)
print("%10f"%123.123)
print("%10s"%"Prakash")
print("Using precision")
print("%.2f"%123.456)
print("%.5f"%123.456)
print("%.2d"%123.456)# Precision do not work on int data type.
print("% d"%123.45678)
print("......................")
print("% 8.3f"%11.7896)
print("%010.5f"%11.7896)
print("%+9.1f"%11.7896)
print("% 5d"%1145)
print("%+5d"%1145)
print("%d"%123456789)
print("% 9.2s"%"Prakash")
print("% 9.4s"%"Prakash")
print("%+9.5s"%"Prakash")
print("%+s"%"Prakash") # + flag do not work on string data type.
print("Python doesn't loss the data")
print("%+6.1f"%123456789.123)
#print("% 8.2f"%12.9876543210)
