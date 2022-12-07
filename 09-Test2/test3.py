with open("TP.txt", "r") as f:
    whole_text = f.read()

out = []

def word_finder(f, ll):
    w_by_w = whole_text.split()


    for i in w_by_w:


        if i.startswith(f) and i.endswith(ll):

            out.append(i)
    return out

print(word_finder('m', 'g'))
print(word_finder('w', 's'))









# w_by_w = whole_text.split()
# for i in w_by_w:
#     if i.startswith('m') and i.endswith('g'):
#         print(i)

