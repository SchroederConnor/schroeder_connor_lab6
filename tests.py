import subprocess
import sys
import re
import os
import difflib

# -----------------------------
# Remove comments + clean code
# -----------------------------
def remove_comments(text):
    text = re.sub(r'//.*', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text


def print_result(test_name, passed):
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {test_name}")


# -----------------------
# File Checks
# -----------------------

REQUIRED_FILES = [
        "restaurant.h",
        "restaurant.cpp",
        "menuItem.h",
        "menuItem.cpp",
        "main.cpp",
        "Output.txt"
    ]
EXEC = "./restaurant"
# -----------------------------
# Check required files
# -----------------------------
def check_files():
    print("Checking required files...")
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:", ", ".join(missing))
        return False
    return True


# -----------------------------
# Check menuItem.h file
# -----------------------------
def check_menuItem_header():
    print("Checking menuItem.h...")
    with open("menuItem.h") as f:
        header = remove_comments(f.read())

    checks = [
    (r"void\s+operator\s*-\s*\(\s*double\s*\)", "void operator-(double)"),
    (r"MenuItem\s+operator\s*\+\s*\(\s*const\s+MenuItem\s*&\s*\)", "MenuItem operator+(const MenuItem&)"),
    (r"friend\s+ostream\s*&\s*operator\s*<<\s*\(\s*ostream\s*&\s*,\s*const\s*MenuItem\s*&\s*\)", "friend ostream& operator<<(ostream&, const MenuItem&)")
    ]

    checks2 = [
        
        (r"displayMenuItemData", "displayMenuItemData"),
    
    ]

    for regex, label in checks:
        if not re.search(regex, header):
            print("Missing:", label)
            return False
    
    for regex, label in checks2:
        
        if  re.search(regex, header):
            print("There should not be any displayMenuItemData method declaration")
            return False
    
    return True



    


# -----------------------------
# Check menuItem.cpp file
# -----------------------------
def check_menuItem_cpp():
    print("Checking menuItem.cpp...")
    with open("menuItem.cpp") as f:
        cpp = remove_comments(f.read())

 
    checks = [
        
    (r"void\s+MenuItem\s*::\s*operator\s*-\s*\(\s*double\s*", "void MenuItem::operator-(double)"),
    (r"MenuItem\s+MenuItem\s*::\s*operator\s*\+\s*\(\s*const\s+MenuItem\s*&\s*", "MenuItem MenuItem::operator+(const MenuItem&)"),
    (r"ostream\s*&\s*operator\s*<<", "ostream& operator<<(ostream&, const MenuItem&)")
    ]
    for regex, label in checks:
        if not re.search(regex, cpp):
            print("Missing:", label)
            return False
    
    checks2 = [
        
        (r"displayMenuItemData", "displayMenuItemData"),
    
    ]

    for regex, label in checks2:
        if  re.search(regex, cpp):
            print("There should not be any displayMenuItemData method implementation")
            return False
    return True
   
# -----------------------------
# Check restaurant.h file
# -----------------------------
def check_restaurant_header():
    print("Checking restaurant.h...")
    with open("restaurant.h") as f:
        header = remove_comments(f.read())

    checks = [
    
    (r"void\s+operator\s*\+\s*\(\s*const\s+MenuItem\s*&\s*\)", "void operator+(const MenuItem&)"),
    (r"friend\s+ostream\s*&\s*operator\s*<<\s*\(\s*ostream\s*&\s*,\s*const\s*Restaurant\s*&\s*\)", "friend ostream& operator<<(ostream&, const Restaurant&)")
    ]

    checks2 = [
        
        (r"displayRestaurantData", "displayRestaurantData"),
    
    ]

    for regex, label in checks:
        if not re.search(regex, header):
            print("Missing:", label)
            return False
    
    for regex, label in checks2:
        
        if  re.search(regex, header):
            print("There should not be any displayRestaurantData method declaration")
            return False
    
    return True



# -----------------------------
# Check restaurant.cpp file
# -----------------------------
def check_restaurant_cpp():
    print("Checking restaurant.cpp...")
    with open("restaurant.cpp") as f:
        cpp = remove_comments(f.read())

 
    checks = [
        
    (r"void\s+Restaurant\s*::\s*operator\s*\+\s*\(\s*const\s+MenuItem\s*&\s*", "void Restaurant::operator+(const MenuItem&)"),
    (r"ostream\s*&\s*operator\s*<<", "ostream& operator<<(ostream&, const Restaurant&)")
    ]
    for regex, label in checks:
        if not re.search(regex, cpp):
            print("Missing:", label)
            return False
    
    checks2 = [
        
        (r"displayRestaurantData", "displayRestaurantData"),
    
    ]

    for regex, label in checks2:
        if  re.search(regex, cpp):
            print("There should not be any displayMenuItemData method implementation")
            return False
    if "Limit exceeded!" not in cpp:
        print("Missing overflow error message in addItem()")
        return False
   
    return True

# -----------------------
# addItem capacity check
# -----------------------
def addItem_check():
    print("Checking addItem method...")
    with open("restaurant.cpp") as f:
        cpp = remove_comments(f.read())
    if "Limit exceeded!" not in cpp:
        print("Missing overflow error message in addItem()")
        return False
    return True

# -----------------------------
# Check main file
# -----------------------------
def check_main():
    print("Checking main.cpp...")

    with open("main.cpp", "r") as f:
        content = remove_comments(f.read())

    check = [
        
        "displayRestaurantData",
        "addItem",
        "[",
        "]"
    ]

    # for regex, label in check:
    #     if re.search(regex, content):
    #         print("Remove:", label)
    #         return False
    # return True

    found = [r for r in check if r in content]

    if  found:
        
        for m in found:
            print("Remove:", m)
        
        return False
    

    checks = [
   

    (r'burger\s*-\s*2\.5\s*;', 
     'Apply discount using operator-'),


    (r'restaurant\s*\+\s*burger\s*;', 
     'restaurant + burger'),

    (r'restaurant\s*\+\s*pizza\s*;', 
     'restaurant + pizza'),

    (r'restaurant\s*\+\s*sandwich\s*;', 
     'restaurant + sandwich'),

    (r'restaurant\s*\+\s*softDrink\s*;', 
     'restaurant + softDrink'),

    (r'MenuItem\s+combo\s*=\s*(?:burger\s*\+\s*softDrink|softDrink\s*\+\s*burger)\s*;', 
     'Create combo using operator+'),

    (r'combo\s*\.\s*setName\s*\(\s*"Combo\s*\(Burger\s*&\s*Drinks\)"\s*\)', 
     'Set combo name'),

    (r'restaurant\s*\+\s*combo\s*;', 
     'restaurant + combo'),

    

    (r'restaurant\s*\+\s*salad\s*;', 
     'restaurant + salad'),

    (r'cout\s*<<\s*restaurant\s*;', 
     'Display restaurant using <<')
    ]
    for regex, label in checks:
        if not re.search(regex, content):
            print("Missing:", label)
            return False
    return True


# -----------------------------
# Build project
# -----------------------------
def build():
    print("Building project...")

    result = subprocess.run(["make"], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Build failed:\n")
        print(result.stderr)
        return False 
    return True


# -----------------------------
# Run program
# -----------------------------
def run_program():
    print("Running program...")

    if not os.path.exists(EXEC):
        print(" Executable not found")
        sys.exit(1)

    result = subprocess.run([EXEC], capture_output=True, text=True)

    if result.returncode != 0:
        print(" Program crashed")
        print(result.stderr)
        sys.exit(1)

    print("Program output captured.")
    return result.stdout.strip()


# ---------------------------
# Run make clean
# ---------------------------
def check_make_clean():
    try:
        subprocess.run(
            ["make", "clean"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        obj_files = [f for f in os.listdir(".") if f.endswith(".o")]
        exe_files = os.path.exists(EXEC)
        # if not os.path.exists(EXEC):
            
        #     sys.exit(1)
        print ("Checking make clean...")

        if exe_files:
            print("Executable restaurant is not removed.")
            return False 

        if obj_files:
            print("Not all the .o files are removed.")
            return False

        return True

    except Exception:
        return False


# -----------------------------
# Load expected output
# -----------------------------
def load_expected():
    with open("Output.txt", "r") as f:
        return f.read().strip()


# -----------------------------
# Compare outputs
# -----------------------------
def compare_output():
    print("Comparing output with Output.txt...")

    actual = run_program()
    expected = load_expected()

    if actual == expected:
        print("Output matches exactly!")
        return True
    print("Output does NOT match!\nCheck output.txt")
    
# print(" Output does NOT match!\n")

    diff = difflib.unified_diff(
    expected.splitlines(),
    actual.splitlines(),
    fromfile="Expected (Output.txt)",
    tofile="Actual (Program Output)",
    lineterm=""
    )

    print("Difference Report:")
    print("  --- : Expected output")
    print("  +++ : Your program output")
    print("  -   : Line missing or incorrect in your output")
    print("  +   : Line produced by your program that differs from expected")
    print("      : Lines without a symbol match in both outputs")
    print()

    for line in diff:
        if line.startswith("@@"):
            continue
        print(line)
    return False

# -----------------------------
# Main
# -----------------------------
def main():
    total = 0
    passed = 0

    

    tests = [
        ("Required Files Exist", check_files),
        ("MenuItem Header Declarations", check_menuItem_header),
        ("MenuItem CPP Implementations", check_menuItem_cpp),
        ("Restaurant Header Declarations", check_restaurant_header),
        ("Restaurant CPP Implementations", check_restaurant_cpp),
        
        ("main.cpp Structure", check_main),
        ("Makefile Builds", build),
        ("Executable Created and Output Matching", compare_output),
        ("Make Clean Works", check_make_clean),
        
        
    ]

    for name, func in tests:
        total += 1
        result = func()
        print_result(name, result)

        if result:
            passed += 1

    if passed == total:
        print("\n======================")
        print("Project Passed")
        print("======================")
        sys.exit(0)
    else:
        print("\n======================")
        print("Project Failed")
        print("======================")
        sys.exit(1)
   


if __name__ == "__main__":
    main()