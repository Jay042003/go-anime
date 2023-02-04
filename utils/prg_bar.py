import colorama

def progress_bar(progress, total, color = colorama.Fore.YELLOW):
    percent =  100* (progress /float(total))
    bar = "▉" * int(percent) + "-" * (100 - int(percent))
    print(color + f"\r{bar}| {percent:.2f}%", end ="\r")
    if progress == total:
       print(colorama.Fore.GREEN + f"\r{bar}| {percent:.2f}%", end ="\r") 

print(colorama.Fore.RESET)