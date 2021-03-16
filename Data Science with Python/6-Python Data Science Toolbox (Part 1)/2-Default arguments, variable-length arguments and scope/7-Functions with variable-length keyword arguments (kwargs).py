
def report_status(**kwargs):
    print("\nBEGIN: REPORT\n")

    for key, value in kwargs.items():
        print(key + ": " + value)
    print("\nEND REPORT\n")

report_status(name="luke", affiliation="jedi", status="missing")
report_status(name="anakin", affiliation="sith lord", status="deceased")