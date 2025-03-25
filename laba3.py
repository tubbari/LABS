import re

def sum_monetary_amounts(text):
    amounts = re.findall(r'\$\d+(?:\.\d+)?', text)
    float_amounts = [float(amount[1:]) for amount in amounts]
    return sum(float_amounts)

text = "first amount is $123.45, second amount is $400"
result = sum_monetary_amounts(text)
print(result)
def cleanup_python_code(code):
    code = re.sub(r'#.*', '', code)
    code = re.sub(r'^\s*\r?\n', '', code, flags=re.MULTILINE)
    return code

code = """
# Це коментар
print("Hello")

# Ще один коментар

print("World")
"""

cleaned_code = cleanup_python_code(code)
print(cleaned_code)
print(cleaned_code)
def convert_date_format(date_str):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date_str)

date_str = "2005-11-14"
converted_date = convert_date_format(date_str)
print(converted_date)