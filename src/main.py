import re


CONTACT_LIST_NAME = 'Prediction Kings'
print("Writing to contact_list.vcf. . .")
with open("contact_list.txt", "r") as fileh:
    with open("output/contact_list.vcf", "a", newline="") as vcf_handler:
        for index, phone_number in enumerate(fileh.readlines()):
            name = f"{CONTACT_LIST_NAME} #{index+1}"
            vcf_template = f"""BEGIN:VCARD
            VERSION:3.0
            N:;{name};;;
            FN:{name}
            TEL;TYPE=CELL:{phone_number.strip()}
            END:VCARD
            """
            vcf_template = re.sub(r' ', "", vcf_template)
            vcf_handler.write(vcf_template)
        vcf_handler.close()
    fileh.close()
print("Done writing, vcf saved")
