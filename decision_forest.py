
"""260201016"""
# DECİSİON TREE A
lstat = float(input("Enter lstat value : "))
if lstat >= 9.7:
    if lstat >= 20:
        nox = float(input("Enter nox value : "))
        if nox >= 0.6:
            dta = 10
        else:
            dta = 17
    if lstat < 20:
        dta = 18
if lstat < 9.7:
   rm = float(input("Enter rm value : "))
   if rm < 6.9:
           age = float(input("Enter age value : "))
           if age < 88:
               if rm < 6.6:
                   dta = 23
               else:
                   dta = 28
           else:
               dta = 36
   if rm >= 6.9:
           if rm < 7.4:
               dta = 34
           else:
               dta = 45
print("The value of decision tree A is", dta)

#DECİSİON TREE B
rm = float(input("Enter rm value : "))
if rm < 7.1:
   lstat = float(input("Enter lstat value : "))
   if lstat >= 15:
       nox = float(input("Enter nox value : "))
       if nox >= 0.6:
           if lstat >= 20:
               dtb = 10
           else:
               dtb = 15
       else:
           dtb = 18
   if lstat < 15:
      if rm < 6.5:
          if lstat >= 9.6:
              dtb = 21
          else:
              dtb = 24
      if rm >= 6.5:
          if lstat >= 4.9:
              dtb = 26
          else:
              dtb = 32
if rm >= 7.1:
   if rm < 7.4:
     dtb = 33
   else:
       dtb = 46
print("The value of decision tree B is", dtb)      

#DECİSİON TREE C
rm = float(input("Enter rm value : "))
if rm < 6.7:
    lstat = float(input("Enter lstat value : "))
    if lstat >= 14:
        crim = float(input("Enter crim value : "))
        if crim >= 7:
            dtc = 12
        else:
            dtc = 17
    else:
        if lstat >= 9.5:
            dtc = 21
        else:
            rad = float(input("Enter rad value : "))
            if rad < 7.5:
                dtc = 24
            else:
                dtc = 34
else:
    if rm < 7.5:
        lstat = float(input("Enter lstat value : "))
        if lstat > 5.5:
            ptratio = float(input("Enter ptratio value : "))
            if ptratio >= 19:
                dtc = 22
            else:
                dtc = 31
        else:
            dtc = 34
    else:
        dtc = 45
print("The value of decision tree C is", dtc) 

print("The average value is", (dta+dtb+dtc)/3)       
       
        
       
               
               
