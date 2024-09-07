# Developer : Sadra Abbaszadeh
# آینده ای که در انتظار ما هست فراتر از این حرفاست!

#بخش کتابخانه ها 
import random #----> کتابخانه رندوم
import threading #----> کتابخانه ترد ( پردازش موازی)
# بخش قفل مورد استفاده در پردازش موازی
lock = threading.Lock()
#پیام خوش آمد گویی
print("khos Amadid ")
#بخش قوانین
def Ghavanin():
    lock.acquire()
    print("""Ghavanin Bazi :
       1. Shoma Faghat 7 Bar shans Hads Darid
       2. Darsorat Hads Dorost 1 emtiyaz Daryaft Mikonid
       3. Computer 5 Bar Emkan Hads adad Shoma Ra Darad
       4. HarGone Taghalob Baes Ban Shodan Shoma Mishavad
       """)
    lock.release()
#بخش ثبت نام
def bazi():
    # global جهت سراسری کردن متغیر داخل تابع بازی
    global name
    global player_number
    global number
    # انتخاب کاربر برای بازی کردن یا نکردن
    select = input("Salam Mikhahid To bazi sherkat Konid: (please Type Yes Or No) ")
    # شرط بررسی انتخاب کاربر اگر برابر با yes بود
    if select.lower() == "yes":
        # به کاربر یک شماره پلیری میده ما بین 1و10
            player_number = random.randint(1, 10)
            #کاربر اینجا نام خود را وارد میکنه
            name = input("Lotfan Name khod ra vared konid: ")
            # خوش آمد گویی با نام کاربر
            print(f"{name} Khos omadi be Bazi! Omidvaram shoma barande bashid :)")
            # نمایش دادن شماره به پلیر همراه نام
            print(f"Player {name} Shomare Shoma: {player_number}")
            #پیام اماده سازی بازی
            print("Bazi Shoma darhal Amade Sazi")
            #عدد انتخابی توسط کاربر برای حدس کامپیوتر
            number = int(input("Lotfan yek adad to range(20, 60) befrestid: "))
            # شرط بررسی انتخاب کاربر در رنج تعیین شده
            if number not in range(20,61):
                #نمایش دادن پیام ارور
                print("Error")
                #بررسی شرط  برقرار بودن عدد خواسته شده در رنج
            elif number in range(20,61):
                print(f"Adad entekhabi Shoma: {number} Ye razi begham? ghrar Hast to Hads bezani Va bad computer :)")
                HadsUser()
                HadsPC()
    # بررسی انتخاب کاربر قبل از انتخاب عدد
    elif select.lower() == "no":
            print("Narahat Shodam Enshallah Dafe Bad :)")
    else:
            print("Please Type Valid Text")
## بخش حدس زدن کامپیوتر
#تابع حدس pc
def HadsPC():
    #تعداد شانس های حدس برای کامپیوتر
    shanspc = 6
    # تعداد حدس زده pc رو صفر قرار میدیم 
    tedadhadszadepc = 0
    # تعیین حلقه تکرار تا زمانی که تعداد حدس زده pc از شانس های حدسش پایین تر باشد
    while tedadhadszadepc < shanspc:
        # شماره انتخابی رندوم توسط کامپیوتر
        pc_random = random.randint(20,61)
        #اضافه شدن  به تعداد حدس زده pc هنگام هربار حدس زدن تا محدودیت درست کار کند
        tedadhadszadepc+=1
        if pc_random < number: #-----> بررسی شرط برای کامپیوتر
            print("< number")
        elif pc_random > number:
            print("> number")
        elif pc_random == number:
            emtiyazpc = 1
            print(f"PC {emtiyazpc} Emtiyaz Daryaft Kard") # -----> اگر کامپیوتر برنده شده باشد یک امتیار دریافت میکند
            break #-----> توقف این حلقه بعد از دریافت امتیاز
    else:
            print("bakhti PC")
 ##بخش حدس زدن کاربر
 #تابع حدس توسط کاربر
def HadsUser():
    #تعداد شانس های موجود
    Shans = 6
    #تعداد حدس زده رو صفر قرار میدهیم
    tedadhadszade = 0
    #عدد رندوم انتخاب شده توسط کامپیوتر تا کاربر حدس بزنه
    Number2 = random.randint(1, 50)
    # ساخت حلقه تکراری که تا زمانی که تعداد حدس زده ها از shans کمتر باشد ادامه پیدا کند
    while tedadhadszade < Shans:
        guess = int(input(f"lotfan adad hadsi khod ra to range (1,50) Befrestid Tavajoh Dasthe Bashid Shoma Fagaht {Shans} shans Darid : adad ra vared konid   :  "))
        tedadhadszade += 1
        if guess < Number2:
            print(f"your number : {guess} , adad Hads Zade Shoma Kochektar az adad computer Mibasahad")
        elif guess > Number2:
            print(f"your number : {guess} , adad Hads Zade Shoma Bozorgh az adad computer Tar Mibashad ")
        elif guess == Number2:
            emtiyaz = 1
            print(f"{name} Mohtaram Ba Shomare {player_number} Barande Shodid Va {emtiyaz} Emtiyaz Daryaft Krdid")
            break
    else:
        print(f"{name} mohtaram Shoma Bakhtid :( adad Entekhabi Computer {Number2}")
#این بخش بررسی می‌کند که آیا برنامه به عنوان ماژول اصلی اجرا شده است یا فقط به عنوان یک ماژول فراخوانی شده است
if __name__ == "__main__":
    # تعریف دو رشته برای اجرای موازی کد
    target1 = threading.Thread(target=Ghavanin)
    target3 = threading.Thread(target=bazi)
# شروع اجرای رشته‌ها
    target1.start()
    target3.start()
# انتظار تا اجرای رشته‌ها به پایان برسد
    target1.join()
    target3.join()

