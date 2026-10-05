import os
import shutil

try:
    # گرفتن آدرس از کاربر و حذف فاصله‌ها یا کاراکترهای اضافی
    file_location = input("Enter The Folder's Address: ").strip(' "\'')
    # استانداردسازی مسیر (برای رفع مشکل اسلش آخر)
    file_location = os.path.normpath(file_location) 

    # استفاده از Set برای جلوگیری از پسوندهای تکراری
    file_types = set()

    files = os.listdir(file_location)

    # پیدا کردن پسوند فایل‌ها و ساخت پوشه‌ها
    for item in files:
        item_path = os.path.join(file_location, item)
        # فقط در صورتی که آیتم یک "فایل" باشد بررسی می‌شود
        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1].lower() # تبدیل به حروف کوچک
            if ext: # اگر فایل دارای پسوند بود
                folder_name = ext[1:] # حذف نقطه از اول پسوند
                file_types.add(folder_name)

    # ساخت پوشه‌ها
    for folder_name in file_types:
        folder_path = os.path.join(file_location, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    # انتقال فایل‌ها به پوشه‌های مربوطه
    for item in files:
        item_path = os.path.join(file_location, item)
        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1].lower()
            if ext:
                folder_name = ext[1:]
                dest_dir = os.path.join(file_location, folder_name)
                dest_file = os.path.join(dest_dir, item)
                
                # جلوگیری از ارور در صورت وجود فایل هم‌نام در مقصد
                if not os.path.exists(dest_file):
                    # استفاده از shutil.move امن‌تر از os.rename است
                    shutil.move(item_path, dest_dir)

    # پیدا کردن مسیر دسکتاپ کاربر فعلی به صورت خودکار (داینامیک)
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    folder_name = os.path.basename(file_location)
    zip_destination = os.path.join(desktop_path, f"{folder_name}_Sorted")

    # فشرده‌سازی پوشه مرتب‌شده
    shutil.make_archive(zip_destination, 'zip', os.path.dirname(file_location), folder_name)

    print(f'Done! Zipped Folder ({folder_name}_Sorted.zip) Is On Your Desktop!')
    
except FileNotFoundError:
    print("Error: Invalid Address or Folder Not Found!")
except PermissionError:
    print("Error: You don't have permission to access or modify these files.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
