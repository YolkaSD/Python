l = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
     {" VIII ": " S007 "}]
set_uniq = set()

for dct in l:
    for v in dct.values():
        set_uniq.add(v.strip())
print(set_uniq)
